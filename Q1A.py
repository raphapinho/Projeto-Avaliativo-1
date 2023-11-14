"""1. A partir do programa visto em sala de aula: cap1_prog2.py para visualização do vetor
campo elétrico de uma carga pontual adapte o mesmo para: a) Fazer com a magnitude
do campo elétrico em cada ponto de observação seja a mesma.  
"""


from vpython import *

#from visual import *


usqpez = 9e9
qe = 1.6e-19
fe = 3e-16

font = sphere(pos = vector(0,0,0), radius = 1e-9, color =  color.red)
q_font = 2*pi


tetamax = 2*pi
dteta = pi/10
R = 1e-8
teta = 0

while teta < tetamax:
    rate(500)
    r_obs = R * vector(cos(teta), cos(pi/2-teta), 0)
    r = r_obs - font.pos
    rchap = r/mag(r)

    E1 = (usqpez * q_font/mag(r)**2)*rchap

    arrow(pos = r_obs, color = color.yellow, axis = fe*E1/6, shafwidth = font.radius/4)
    teta = teta + dteta

while True:
    rate(30)