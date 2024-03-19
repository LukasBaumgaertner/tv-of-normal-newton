FROM quay.io/fenicsproject/stable:latest
RUN apt update && apt install libglapi-mesa && apt install -y libgl1-mesa-glx 
RUN apt install libxcursor1 && apt install libxinerama1 && apt install libglu1-mesa
RUN pip3 install --upgrade pip && pip3 install --upgrade numpy==1.19.5
WORKDIR /data
RUN wget https://www.paraview.org/files/v5.12/ParaView-5.12.0-MPI-Linux-Python3.10-x86_64.tar.gz
WORKDIR /usr/local
RUN tar -xzf /data/ParaView-5.12.0-MPI-Linux-Python3.10-x86_64.tar.gz --strip-components=1 
WORKDIR /data
RUN wget https://gmsh.info/bin/Linux/gmsh-3.0.6-Linux64.tgz
WORKDIR /usr/local
RUN tar -xf /data/gmsh-3.0.6-Linux64.tgz --strip-components=1 
WORKDIR /home/fenics/shared
RUN echo "export PVPYTHON=pvpython" >> /home/fenics/.profile
RUN echo "export GMSH=gmsh" >> /home/fenics/.profile 
