import sys
sys.path.append('../../')
import dolfin as df
import utils.utils
from AugmentedLagrangianRiemanian import AugmentedLagrangian
from smooth_update import GradientDescent
from ADMM import ADMM

mesh = utils.utils.ReadMeshH5("../fandisk.h5") 
AL = AugmentedLagrangian(mesh)


beta = 0.03
tau = 2e-8
rho = 1.0





AL = AugmentedLagrangian(mesh, rho = rho, beta = beta, tau = tau)

#from IPython import embed; embed()

fout = df.XDMFFile(df.MPI.comm_world, "output/Classic.xdmf")
fout.parameters["flush_output"] = True
fout.parameters["rewrite_function_mesh"] = True

def cb(AL, i):
    fout.write(AL.movefun, float(i))

ADMM(AL,GradientDescent,cb = cb, max_outer_iter = 1000, max_inner_iter=3)

