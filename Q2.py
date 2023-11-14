"""2. Implemente um programa em Python para visualização das linhas de força do campo
elétrico entre quatro cargas pontuais sobre o plano xy separados por uma certa
distância (adapte o programa visto em sala de aula para duas cargas pontuais). As
cargas devem ser (+q,-q,+q,-q). """

from vpython import *

usqpez = 9e9
qe = 1.6e-19
fe = 3e-16

fonte1 = sphere(pos=vector(0.3e-8, 0.3e-8, 0), radius=1e-9, color=color.blue)
q_fonte1 = +qe

fonte2 = sphere(pos=vector(0.6e-8, 0.6e-8, 0), radius=1e-9, color=color.red)
q_fonte2 = -qe

fonte3 = sphere(pos=vector(0.4e-8, 0.7e-8, 0), radius=1e-9, color=color.green)
q_fonte3 = +qe

fonte4 = sphere(pos=vector(0.7e-8, 0.4e-8, 0), radius=1e-9, color=color.yellow)
q_fonte4 = -qe

tetamax = 2 * pi
dteta = pi / 16
R = 1e-8
teta = 0

while teta < tetamax:
    rate(500)
    r_obs = R * vector(cos(teta), sin(teta), 0)
    r1 = r_obs - fonte1.pos
    r2 = r_obs - fonte2.pos
    r3 = r_obs - fonte3.pos
    r4 = r_obs - fonte4.pos

    E1 = (usqpez * q_fonte1 / mag(r1) ** 2) * norm(r1)
    E2 = (usqpez * q_fonte2 / mag(r2) ** 2) * norm(r2)
    E3 = (usqpez * q_fonte3 / mag(r3) ** 2) * norm(r3)
    E4 = (usqpez * q_fonte4 / mag(r4) ** 2) * norm(r4)

    Er = E1 + E2 + E3 + E4

    arrow(pos=r_obs, color=color.red, axis=fe * Er / 6, shaftwidth=fonte1.radius / 4)
    teta = teta + dteta
