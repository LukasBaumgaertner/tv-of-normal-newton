import sys
sys.path.append('../')
import dolfin as df
import utils.utils as utils
import numpy as np

mesh = df.Mesh("remeshed_cube.xml")
mesh.init()
subdomain = df.MeshFunction("size_t", mesh, "remeshed_cube_physical_region.xml")
utils.Orientate(mesh)



CG = df.FunctionSpace(mesh, "CG", 1)
f = df.Function(CG)
fvec = np.ones(f.vector().get_local().size)
dofmap = CG.dofmap()
print(subdomain.size(), mesh.num_vertices(), mesh.num_cells())
for c in df.cells(mesh):
    for v in c.entities(0):
        if subdomain[c.index()] == 0:
            dof = dofmap.entity_dofs(mesh, 0, [v])[0]
            fvec[dof] = 0.0
f.vector().set_local(fvec)

df.File("initial_cube.pvd") << f


file = utils.SaveMeshH5(mesh,"remeshed_cube.h5", closeFile = False)
file.write(f, "vertices")
file.close()
