import dolfin as df
import sys
sys.path.append('../utils')
import utils

f = utils.ReadObj("../meshes/bunny.obj")
df.File("bunny_clean.pvd") << f

mesh = f.function_space().mesh()
utils.Orientate(mesh)
utils.AddNoise2Mesh(mesh)
utils.SaveMeshH5(mesh,"bunny.h5")

df.File("bunny_noise.pvd") << f
