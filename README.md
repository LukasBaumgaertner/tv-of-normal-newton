This repository contains code corresponding to the paper 

  Baumgärtner, Bergmann, Herzog, Schmidt, Vidal-Núñez, Weiß

  Mesh Denoising and Inpainting using the Total Variation of the Normal and a Shape Newton Approach
  arxiv: [2012.11748](https://arxiv.org/abs/2012.11748)

The code requires the latest installation of (legacy) fenics as well as gmsh 3.0.6 (at \$GMSH) and Paraview python (at \$PVPYTHON).
To add orientation, noise and remeshing for the respective testcases, run
```bash
bash prepare.sh
```
To run all experiments, one after the other, run
```bash
bash runexperiments.sh
```
This usually takes about 2-3 hours and 3GB of disk spcae. Single experiments can be run by e.g. `python3 ./FandiskDenoising/Newton/test.py`

In order to resolve the dependencies, it is advised to run the code inside a Docker container, following the included `Dockerfile`: 
```bash
docker build -t tv_of_normal .
docker run -ti -v $(pwd):/home/fenics/shared tv_of_normal "bash prepare.sh"
docker run -ti -v $(pwd):/home/fenics/shared tv_of_normal "bash runexperiments.sh"
```
Afterwards, the results can be viewed in paraview, e.g. by 
```bash
paraview ./visualizations/pv_FandiskDenoising.py  
```
To reproduce the plots go to `./plots` and compile `plots.tex`.
