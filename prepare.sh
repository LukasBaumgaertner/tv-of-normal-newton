#!/bin/bash
echo "Preparing meshes"
cd Bunny
python3 add_noise_and_orientation.py
cd ..

cd FandiskDenoising
python3 add_noise_and_orientation.py
cd ..

cd FandiskInpainting
python3 remesh_inp_areas.py
cd ..

cd UnitCube
python3 remesh_inp_areas.py
cd ..

echo "Preparing meshes done."
