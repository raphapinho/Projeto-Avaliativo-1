"""b) Adapte o programa
para colocar duas cargas iguais do elétron e positivas (como está definida no
programa) só que uma na posição (-0,5x10-8, 0, 0) e outra na posição (0,5x10-8,0,0) e a
partir do centro (0,0,0) faça um circulo de raio R de observação no plano que englobe
as duas cargas e desenhe o campo elétrico resultante das duas cargas nesse círculo
(gere pelo menos dez valores). A seguir um diagrama esquemático da geometria da
questão b)"""

from vpython import *

usqpez = 9e9
qe = 1.6e-19
fe = 3e-16

fonte1 = sphere(pos = vector(-0.5e-8, 0, 0), radius = 1e-9, color = color.blue)
q_fonte1 = qe

fonte2 = sphere(pos = vector(0.5e-8, 0, 0), radius = 1e-9, color = color.blue)
q_fonte2 = -qe

tetamax = 2 * pi
dteta = pi/16
R = 1e-8
teta = 0

while teta < tetamax:
    rate(500)

    r_obs = R * vector(cos(teta), sin(teta), 0)

    r1 = r_obs - fonte1.pos
    r2 = r_obs - fonte2.pos

    rchap1 = r1/mag(r1)
    rchap2 = r2/mag(r2)

    E1 = (usqpez * q_fonte1 / mag(r1) ** 2) * rchap1
    E2 = (usqpez * q_fonte2 / mag(r2) ** 2) * rchap1

    Er = E1 + E2

    arrow(pos = r_obs, color = color.blue, axis = fe* Er/ 6, shafwidth = fonte1.radius / 4)
    teta = teta + dteta

while True:
    rate(30)