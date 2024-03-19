import sys
sys.path.append('../')
import dolfin as df
import utils.utils as utils

mesh = df.Mesh("../meshes/fandisk.xml")

f = df.Function(df.FunctionSpace(mesh, "CG", 1))
df.File("fandisk_clean.pvd") << f
utils.Orientate(mesh)
utils.AddNoise2Mesh(mesh)
utils.SaveMeshH5(mesh,"fandisk.h5")
df.File("fandisk_noise.pvd") << f

