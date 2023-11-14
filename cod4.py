from vpython import *

scene.width = scene.height = 800
oofpez = 9e9
qe = 1.6e-19
sf = 5e-20
source_01 = sphere (pos =vector (0, 0.1e-9, 0) ,
color = color.red,radius = 0.5e-10)
q_01 = +qe

source_02 = sphere (pos =vector (0, 0.1e-9, 0) ,
color = color.red,radius = 0.5e-10)
q_02 = -qe