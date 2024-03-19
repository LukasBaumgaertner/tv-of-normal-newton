import dolfin as df
df.set_log_level(30)
from utils.shape_identities import log, dlog, divE
import numpy as np
import ufl
import time

class AugmentedLagrangian():
    def __init__(self, mesh, rho=1, beta=1, tau=1, tracked_vertices = None, fixed_vertices = None, shape_first = True):
        
        # mesh stuff
        self.mesh = mesh
        self.n = df.CellNormal(mesh)
        self.mu = df.FacetNormal(mesh)
        self.tE = df.cross(self.n,self.mu)
        
        # saving parameters, rho potentially changes but we dont want to redefine the forms and thus make it a spatially constant function
        R = df.FunctionSpace(mesh, "R", 0)
        self.rho = df.project(df.Constant(rho), R)
        self.tau = df.Constant(tau)
        self.beta = df.Constant(beta)
        
        #deformation space
        self.CG = df.VectorFunctionSpace(mesh, "CG", 1)
        #test and trial functinos for shape derivatives
        self.V = df.TestFunction(self.CG)
        self.W = df.TrialFunction(self.CG)
        
        # function that is 1 on tracked vertices and 0 on untracked vertices
        if tracked_vertices == None:
            self.tracked_vertices = df.Constant(1.0)
        else:
            self.tracked_vertices = tracked_vertices
            
        # Boundary condition that can set vertex movement to 0 if vertices are fixed        
        if fixed_vertices == None:
            self.fixed_vertices = 1
        else:
            self.fixed_vertices = fixed_vertices
        
        # boolean for update order
        self.shape_first = shape_first
        
        # movefun to move the mesh later
        self.movefun = df.Function(self.CG)
        # help function for shape gradient
        self.shapegrad = df.Function(self.CG)
        
        #save tracking
        self.x = df.SpatialCoordinate(self.mesh)
        self.tracking_data = df.project(self.x, self.CG)
        
        # spaces auxiliary variables
        self.skeletonDG = df.VectorFunctionSpace(mesh, "HDiv Trace", 0)
        # auxiliary variable and multiplier
        self.d = df.Function(self.skeletonDG)
        self.b = df.Function(self.skeletonDG)
        
        #saving old normals for parallel transport
        self.DGspace = df.VectorFunctionSpace(mesh, "DG", 0)
        # fast project without solve
        self.n_old = df.Function(self.DGspace)
        self.n_old.vector().set_local(df.assemble( df.inner( self.n, df.TestFunction(self.DGspace))/df.CellVolume(self.mesh)*df.dx))
                                                                    
        

        # form for AL
        # fidelity
        self.AL_form = 0.5*(self.x - self.tracking_data)**2*df.dP
        # term to prevent mesh degeneration
        self.AL_form += self.tau/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.AL_form += self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # contraint
        self.AL_form += 0.5*self.rho*(self.d('+') - log(self.n, self.mu) - self.b('+'))**2*df.dS(domain=mesh) 
        self.AL_form += -0.5*self.rho*self.b('+')**2*df.dS(domain=mesh)

        # derivative of AL
        # fidelity
        self.d_AL_form = df.inner(self.x-self.tracking_data, self.V)*df.dP
        # term to prevent mesh degeneration
        self.d_AL_form += -self.tau*df.div(self.V)/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.d_AL_form += divE(self.tE, self.V)*self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # constraint (element size derivative)
        self.d_AL_form += divE(self.tE, self.V)*0.5*self.rho*(self.d('+') - log(self.n, self.mu) - self.b('+'))**2*df.dS(domain=mesh)
        self.d_AL_form += -divE(self.tE, self.V)*0.5*self.rho*self.b('+')**2*df.dS(domain=mesh)
        # constraint (material derivative)
        self.d_AL_form += self.rho*df.inner(self.d('+') - log(self.n, self.mu) - self.b('+'), -dlog(self.n, self.mu, self.tE, self.V))*df.dS(domain=mesh)
        
        # form for primal residual 
        self.primal_res_form = (log(self.n, self.mu) - self.d('+') )**2*df.dS
            
        # form for dual/shape residual       
        # fidelity
        self.d_L_form = df.inner(self.x-self.tracking_data, self.V)*df.dP
        # term to prevent mesh degeneration
        self.d_L_form += -self.tau*df.div(self.V)/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.d_L_form += divE(self.tE, self.V)*self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # constraint (element size derivative)
        self.d_L_form += divE(self.tE, self.V)*self.rho*df.inner(self.b('+'), log(self.n, self.mu) - self.d('+'))**2*df.dS(domain=mesh)
        # constraint (material derivative)
        self.d_L_form += self.rho*df.inner(self.b('+'), dlog(self.n, self.mu, self.tE, self.V))*df.dS(domain=mesh)
 
        # list for scalar quantities to be filled by AL.log
        self.history = []
        
        
    # evaluate AL    
    def val(self, vec=None):
        if not vec is None:
            self.set_mesh_coords(vec)
        return df.assemble(self.AL_form)
    
    #evaluate derivative of AL    
    def derivative(self, vec=None):        
        if not vec is None:
            self.set_mesh_coords(vec) 
        return df.assemble(self.d_AL_form)

    # move mesh to input vec    
    def set_mesh_coords(self,vec):
        # set mesh coordinates to vec by moving it by vec - current_cords
        movevec = vec - df.assemble( df.inner(self.x, self.V)*df.dP )
        self.movefun.vector().set_local(movevec)
        df.ALE.move(self.mesh, self.movefun)
        
        
    def get_mesh_coords(self):
        return df.assemble( df.inner(self.x, self.V)*df.dP )

    def update_nonsmooth(self):
        # transport b to current tangent space
        #P_{n_0\to n} (b) = b - 2\frac{b^\top n}{\lvert n_0+n\rvert^2} (n_0+n).
        bvec = df.assemble( df.inner(df.TestFunction(self.skeletonDG), self.b - 2*df.inner(self.b, self.n)/df.inner(self.n_old+self.n,self.n_old+self.n)*(self.n_old+self.n))('+')/df.FacetArea(self.mesh)('+')*df.dS )
        self.b.vector().set_local(bvec)
        
        # compute dofs vector of log + b
        vec = df.assemble( df.inner(df.TestFunction(self.skeletonDG)('+'),log(self.n, self.mu))/df.FacetArea(self.mesh)('+')*df.dS).get_local() + self.b.vector().get_local()
        #compute the norm of log+b on each edge and repeat it in order to normalize log+b 
        normvec = np.repeat( np.sqrt(vec[0::3]**2 + vec[1::3]**2 + vec[2::3]**2), 3) 
        # vectorial shrinkage, fix division by 0, if fix is nessesary the second term will vanish provided beta/rho > tol ...
        dvec = vec/np.maximum(1e-15, normvec)*np.maximum(0,normvec-float(self.beta)/float(self.rho) ) 
        #set dofs to fenics functions 
        self.d.vector().set_local(dvec)


    def update_multipliers(self):
        # compute dofs of b + log  - d
        vec = self.b.vector().get_local() + df.assemble( df.inner(df.TestFunction(self.skeletonDG)('+'),log(self.n, self.mu))/df.FacetArea(self.mesh)('+')*df.dS).get_local() - self.d.vector().get_local()
        # set dofs to b 
        self.b.vector().set_local(vec)
        # save normal corresponding to current b with fast project without solve
        self.n_old.vector().set_local(df.assemble( df.inner( self.n, df.TestFunction(self.DGspace))/df.CellVolume(self.mesh)*df.dx))
        
    def update_tracking(self):
        # update tracked vertex positions to current vertex positions, where self.tracked vertices = 0
        df.solve(inner(self.V, self.W)*dP == self.tracked_vertices*df.inner(self.tracking_data, self.V)*dP + (1-self.tracked_vertices)*df.inner(self.x, self.V)*dP , self.tracking_data)
    
    def update_penalty_param(self):
        pass
        
    def finish_iteration(self):
        pass
        

    def primal_residual(self):
        return np.sqrt(df.assemble(self.primal_res_form))
        
    #requires computation of shape gradient of non-augmented Lagrangian    
    def dual_residual(self):
        df.solve( df.inner(self.V, self.W)*df.dx + 1e-2*df.inner(df.grad(self.V), df.grad(self.W))*df.dx == self.d_L_form, self.shapegrad)
        shape_res_norm = np.sqrt(df.assemble( df.inner(self.shapegrad, self.shapegrad)*df.dx + 1e-2*df.inner(df.grad(self.shapegrad), df.grad(self.shapegrad))*df.dx))
        return shape_res_norm
        
    def log(self, infos):
        pres = self.primal_residual()
        dres = self.dual_residual()
        current_state = [ pres, dres, dres, np.sqrt(pres**2+dres**2) ,float(self.rho), time.time(), *infos]
        self.history += [current_state]
        
