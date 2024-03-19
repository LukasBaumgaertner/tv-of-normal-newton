from dolfin import *
import os
import numpy as np
set_log_level(30)

def recmark(vindex, depth, vec, sub_domain_triangles, visited):
    V = Vertex(mesh, vindex)

    vec[v2d[vindex]] = 1
    
    if depth > 0.1 and (visited[V.index()] < depth-0.1 or visited[V.index()] < 0.1) :
        visited[V.index()] = depth
        for C in V.entities(2):
            sub_domain_triangles[C] = 1
            for v in Cell(mesh, C).entities(0):
                if v != vindex:
                    recmark(v, depth-1, vec,sub_domain_triangles, visited)
    
    if depth < 0.1:
        for C in V.entities(2):
            sub_domain_triangles[C] = 1
        return None

        
mesh=BoundaryMesh(UnitCubeMesh(10,10,10), "exterior")
mesh.init()    

vertlist = [0, 145]

sub_domain_triangles = MeshFunction("size_t", mesh, 2)
removedepth = 3
visitedverts = MeshFunction("size_t", mesh, 0)
CG = FunctionSpace(mesh, "CG", 1)
v2d = vertex_to_dof_map(CG)


removedverts = Function(CG)
vec = removedverts.vector().get_local()
for start in vertlist:      
    recmark(start, removedepth, vec, sub_domain_triangles, visitedverts)



for c in cells(mesh):        
    counter = 0        
    for e in edges(c):  
        index = e.entities(2)[0] + e.entities(2)[1] - c.index()
        if sub_domain_triangles[index] > 0.5:
            counter += 1 
    if counter >= 2:
        sub_domain_triangles[c.index()] = 1
for e in edges(mesh):
    index0 = e.entities(2)[0]
    index1 = e.entities(2)[1]
    if sub_domain_triangles[index0] > 0.5 and sub_domain_triangles[index1] > 0.5:
        for v in vertices(e):
            vec[v2d[v.index()]] = 1

removedverts.vector().set_local(vec)
vec2 = np.ones(vec.size)
for c in cells(mesh):
    for v in c.entities(0):
        if sub_domain_triangles[c.index()]==0:
            vec2[v2d[v]] = 0

VCG = VectorFunctionSpace(mesh, "CG", 1)
V = TestFunction(VCG)
move = Function(VCG)
for i in range(4000):
    move.vector().set_local(-1e-3*assemble( div(V)*dx).get_local()*np.repeat(vec2,3))
    ALE.move(mesh, move)

File("sub_domain_triangles.pvd") << sub_domain_triangles


os.system("$PVPYTHON pv_remove_areas.py")

os.system("$GMSH ./remesh_cube.geo -2 -o remeshed_cube.msh")

os.system("dolfin-convert remeshed_cube.msh remeshed_cube.xml")

os.system('cat remeshed_cube.xml | sed "s/dim=\\"2\\"/dim=\\"3\\"/" > remeshed_cube_fixed.xml')
os.system("rm remeshed_cube.xml")
os.system("mv remeshed_cube_fixed.xml remeshed_cube.xml")

os.system("python3 add_orientation_and_indicator.py")
