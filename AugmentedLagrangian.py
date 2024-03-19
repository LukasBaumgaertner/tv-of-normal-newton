import dolfin as df
df.set_log_level(30)
from utils.shape_identities import logmu, dlogmu, Hlogmu, divE, Hedge, Hsurf
import numpy as np
import ufl
import time

class AugmentedLagrangian():
    def __init__(self, mesh, rho=1, beta=1, tau=1, tracked_vertices = None, fixed_vertices = None, shape_first = False, adapt_penalty = True):
        
        # mesh stuff
        self.mesh = mesh
        self.n = df.CellNormal(mesh)
        self.mu = df.FacetNormal(mesh)
        self.tE = df.cross(self.n,self.mu)
        
        # saving parameters, rho potentially changes but we dont want to redefine the forms and make it a function
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
            self.fixed_BC = None
        else:
            self.fixed_BC = df.DirichletBC(self.CG, df.Constant((0.0,0.0,0.0)), fixed_vertices, 1)

        # save some bools
        self.shape_first = shape_first
        self.adapt_penalty = adapt_penalty

        # movefun to move the mesh later
        self.movefun = df.Function(self.CG)
        # help function for shape gradient
        self.shapegrad = df.Function(self.CG)
        
        #save tracking
        self.x = df.SpatialCoordinate(self.mesh)
        self.tracking_data = df.project(self.x, self.CG)
        
        # spaces auxiliary variables
        self.skeletonDG = df.FunctionSpace(mesh, "HDiv Trace", 0)
        # auxiliary variable and multiplier
        self.d = df.Function(self.skeletonDG)
        self.b = df.Function(self.skeletonDG)

        # functions to solve the log into
        self.log_old = df.Function(self.skeletonDG)
        # fast project without solve
        self.log_old.vector().set_local(df.assemble( df.TestFunction(self.skeletonDG)('+')*logmu(self.n, self.mu)/df.FacetArea(self.mesh)('+')*df.dS)) 

        # form for AL
        # fidelity
        self.AL_form = 0.5*(self.x - self.tracking_data)**2*df.dP
        # term to prevent mesh degeneration
        self.AL_form += self.tau/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.AL_form += self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # contraint
        self.AL_form += 0.5*self.rho*(self.d('+') - logmu(self.n, self.mu) - self.b('+'))**2*df.dS(domain=mesh) 
        self.AL_form += -0.5*self.rho*self.b('+')**2*df.dS(domain=mesh)

        # derivative of AL
        # fidelity
        self.d_AL_form = df.inner(self.x-self.tracking_data, self.V)*df.dP
        # term to prevent mesh degeneration
        self.d_AL_form += -self.tau*df.div(self.V)/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.d_AL_form += divE(self.tE, self.V)*self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # constraint (element size derivative)
        self.d_AL_form += divE(self.tE, self.V)*0.5*self.rho*(self.d('+') - logmu(self.n, self.mu) - self.b('+'))**2*df.dS(domain=mesh)
        self.d_AL_form += -divE(self.tE, self.V)*0.5*self.rho*self.b('+')**2*df.dS(domain=mesh)
        # constraint (material derivative)
        self.d_AL_form += self.rho*df.inner(self.d('+') - logmu(self.n, self.mu) - self.b('+'), -dlogmu(self.n, self.mu, self.V))*df.dS(domain=mesh)
        
        # second derivative of AL
        # fidelity
        self.H_AL_form = df.inner(self.W, self.V)*df.dP
        # term to prevent mesh degeneration        
        self.H_AL_form += -self.tau / df.CellVolume(mesh)**2 * Hsurf(self.n, self.V, self.W) * df.dx(domain=mesh)
        self.H_AL_form += 2*self.tau / df.CellVolume(mesh)**2 * df.div(self.V) * df.div(self.W) * df.dx(domain=mesh)
        # abs term
        self.H_AL_form += Hedge(self.tE,self.V,self.W)*self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # constraint (element size second derivative)
        self.H_AL_form += Hedge(self.tE,self.V,self.W)*0.5*self.rho*(self.d('+') - logmu(self.n, self.mu) - self.b('+'))**2*df.dS(domain=mesh) 
        self.H_AL_form += -Hedge(self.tE,self.V,self.W)*0.5*self.rho*self.b('+')**2*df.dS(domain=mesh)
        # constraint (element size and material mixed second derivative)
        self.H_AL_form += divE(self.tE, self.V)*self.rho*df.inner(self.d('+') - logmu(self.n, self.mu) - self.b('+'), -dlogmu(self.n, self.mu, self.W))*df.dS(domain=mesh) 
        self.H_AL_form += divE(self.tE, self.W)*self.rho*df.inner(self.d('+') - logmu(self.n, self.mu) - self.b('+'), -dlogmu(self.n, self.mu, self.V))*df.dS(domain=mesh) 
        # constraint  (second material derivative)
        self.H_AL_form += self.rho*dlogmu(self.n, self.mu, self.V)*dlogmu(self.n, self.mu, self.W)*df.dS(domain=mesh) 
        self.H_AL_form += self.rho*df.inner(self.d('+') - logmu(self.n, self.mu) - self.b('+'),-Hlogmu(self.n, self.mu, self.tE, self.V, self.W))*df.dS(domain=mesh)
        
        # form for shape residual
        self.d_L_form = self.tracked_vertices*df.inner(self.x-self.tracking_data, self.V)*df.dP
        # term to prevent mesh degeneration
        self.d_L_form += -self.tau*df.div(self.V)/df.CellVolume(mesh)**2*df.dx(domain=mesh)
        # abs term
        self.d_L_form += divE(self.tE, self.V)*self.beta*df.sqrt(self.d('+')**2)*df.dS(domain=mesh)
        # constraint (element size derivative)
        self.d_L_form += divE(self.tE, self.V)*self.rho*df.inner(self.d('+') - logmu(self.n, self.mu), - self.b('+'))*df.dS(domain=mesh)
        # constraint (material derivative)
        self.d_L_form += self.rho*df.inner(self.b('+'), dlogmu(self.n, self.mu, self.V))*df.dS(domain=mesh)
        
        # form for primal residual 
        self.primal_res_form = abs(logmu(self.n, self.mu) - self.d('+') )**2*df.dS
        
        # form for dual residual if computed by projection of subdifferential to 0
        projb = df.conditional(df.le(abs(self.rho*self.b('+')), self.beta), 0, rho*abs(self.b('+'))-self.beta) 
        self.dual_res_form = abs(df.conditional(ufl.le(abs(self.d('+')),1e-8), projb , self.beta*ufl.sign(self.d('+'))-self.rho*self.b('+')))**2*df.dS
        
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
    
    #evaluate Hess of AL
    def Hess(self, vec=None):
        if not vec is None:
            self.set_mesh_coords(vec)
        return df.assemble(self.H_AL_form)

    # move mesh to input vec
    def set_mesh_coords(self,vec):
        # set mesh coordinates to vec by moving it by vec - current_cords
        movevec = vec - df.assemble( df.inner(self.x, self.V)*df.dP )
        self.movefun.vector().set_local(movevec)
        df.ALE.move(self.mesh, self.movefun)
        
    def get_mesh_coords(self):
        return df.assemble( df.inner(self.x, self.V)*df.dP )

    def update_nonsmooth(self):
        # compute dofs vector of log + b
        vec = df.assemble( df.TestFunction(self.skeletonDG)('+')*logmu(self.n, self.mu)/df.FacetArea(self.mesh)('+')*df.dS).get_local() + self.b.vector().get_local()
        #shrink 
        dvec = np.sign(vec)*np.maximum(0,np.abs(vec)-float(self.beta)/float(self.rho) ) 
        #set dofs to fenics functions 
        self.d.vector().set_local(dvec)

    def update_multipliers(self):
        # compute dofs of b + log  - d
        vec = self.b.vector().get_local() + df.assemble( df.TestFunction(self.skeletonDG)('+')*logmu(self.n, self.mu)/df.FacetArea(self.mesh)('+')*df.dS).get_local() - self.d.vector().get_local()
        # set dofs to b 
        self.b.vector().set_local(vec)
        
    def update_tracking(self):
        # update tracked vertex positions to current vertex positions, where self.tracked vertices = 0 (prox term)
        df.solve(df.inner(self.V, self.W)*df.dP == self.tracked_vertices*df.inner(self.tracking_data, self.V)*df.dP + (1-self.tracked_vertices)*df.inner(self.x, self.V)*df.dP , self.tracking_data)
        
    def update_penalty_param(self, factor = 5, scaling = 1.5):
        # update the penalty parameter
        if self.adapt_penalty:
            primal_res = self.primal_residual()
            dual_res = self.nonsmooth_residual()
        
            if primal_res >= factor*dual_res:
                # rho = rho*scaling
                self.rho.assign(self.rho*scaling)
                self.b.assign(self.b/scaling)
                #print("new penalty parameter: ", float(self.rho))
            if dual_res >= factor*primal_res:
                # rho = rho/scaling
                self.rho.assign(self.rho/scaling)
                self.b.assign(self.b*scaling)
                #print("new penalty parameter: ", float(self.rho))
            #print("primalres: ", primal_res, " dualres: ", dual_res)
        
        
    # save log of this iteration
    def finish_iteration(self):
        # after iteration save old log for dual residual
        self.log_old.vector().set_local(df.assemble( df.TestFunction(self.skeletonDG)('+')*logmu(self.n, self.mu)/df.FacetArea(self.mesh)('+')*df.dS))
        self.update_tracking()
    
    def primal_residual(self):
        return np.sqrt(df.assemble(self.primal_res_form))
        
    def nonsmooth_residual(self):
        return np.sqrt(df.assemble( (self.rho*( logmu(self.n, self.mu) - self.log_old('+')))**2*df.dS))

    #requires computation of shape gradient of non-augmented Lagrangian
    def shape_residual(self):
        if self.fixed_BC != None:
            df.solve( df.inner(self.V, self.W)*df.dx + 1e-2*df.inner(df.grad(self.V), df.grad(self.W))*df.dx == self.d_L_form, self.shapegrad, self.fixed_BC)
        else:
            df.solve( df.inner(self.V, self.W)*df.dx + 1e-2*df.inner(df.grad(self.V), df.grad(self.W))*df.dx == self.d_L_form, self.shapegrad)
        shape_res_norm = np.sqrt(df.assemble( df.inner(self.shapegrad, self.shapegrad)*df.dx + 1e-2*df.inner(df.grad(self.shapegrad), df.grad(self.shapegrad))*df.dx))
        return shape_res_norm

    
    def log(self, infos):
        pres = self.primal_residual()
        nsres = self.nonsmooth_residual()
        sres = self.shape_residual()
        current_state = [ pres, nsres, sres, np.sqrt(pres**2+nsres**2+sres**2) ,float(self.rho), time.time(), *infos]
        self.history += [current_state]
        
        
        
