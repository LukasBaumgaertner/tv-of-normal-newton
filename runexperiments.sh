#!/bin/bash
echo "Running Fandisk experiments, Newton -> GD -> RM"

cd FandiskDenoising
cd Newton
python3 test.py
cd ..
cd GradientDescent
python3 test.py
cd ..
cd Riemanian
python3 test.py
cd ..
cd ..

echo "Running Bunny"
cd Bunny
cd Newton
python3 test.py
cd ..
cd ..

echo "Running Cube inpainting"

cd UnitCube
cd Newton
python3 test.py
cd ..
cd ..

echo "Running Fandisk inpainting"
cd FandiskInpainting
cd Newton
python3 test.py
cd ..
cd ..

echo "Finished all experiments"
