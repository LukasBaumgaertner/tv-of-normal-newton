import sys
sys.path.append('../../')
import dolfin as df
import utils.utils
from AugmentedLagrangian import AugmentedLagrangian
from smooth_update import Newton
from ADMM import ADMM

mesh, file = utils.utils.ReadMeshH5("../remeshed_cube.h5", closeFile=False)

CG = df.FunctionSpace(mesh, "CG", 1)
moveable_vertices = df.Function(CG)
file.read(moveable_vertices, "vertices")
boundary_marker = utils.utils.CGdofstoEdgemarker(mesh, moveable_vertices, CG.dofmap())
beta = 0.01
tau = 1e-8
rho = 0.01





AL = AugmentedLagrangian(mesh, rho = rho, beta = beta, tau = tau, tracked_vertices = df.Constant(0.0), fixed_vertices = boundary_marker)

#from IPython import embed; embed()

fout = df.XDMFFile(df.MPI.comm_world, "output/Classic.xdmf")
fout.parameters["flush_output"] = True
fout.parameters["rewrite_function_mesh"] = True

def cb(AL, i):
    fout.write(AL.movefun, float(i))

ADMM(AL,Newton,cb = cb, max_outer_iter = 500, max_inner_iter=3)

