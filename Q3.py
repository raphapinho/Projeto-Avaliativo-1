"""3. Adapte o programa anterior para pedir as cargas e o vetor posição das cargas no plano
xy do usuário de três cargas pontuais e mostre a visualização das linhas de força do
campo elétrico. """

from vpython import *

usqpez = 9e9
fe = 3e-16

q_fonte1 = float(input("Digite a carga da fonte 1 (em coulombs): "))
pos_fonte1 = vector(float(input("Digite a posição x da fonte 1: ")), float(input("Digite a posição y da fonte 1: ")), 0)

q_fonte2 = float(input("Digite a carga da fonte 2 (em coulombs): "))
pos_fonte2 = vector(float(input("Digite a posição x da fonte 2: ")), float(input("Digite a posição y da fonte 2: ")), 0)

q_fonte3 = float(input("Digite a carga da fonte 3 (em coulombs): "))
pos_fonte3 = vector(float(input("Digite a posição x da fonte 3: ")), float(input("Digite a posição y da fonte 3: ")), 0)

fonte1 = sphere(pos=pos_fonte1, radius=1e-9, color=color.blue)
fonte2 = sphere(pos=pos_fonte2, radius=1e-9, color=color.orange)
fonte3 = sphere(pos=pos_fonte3, radius=1e-9, color=color.purple)

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

    E1 = (usqpez * q_fonte1 / mag(r1) ** 2) * norm(r1)
    E2 = (usqpez * q_fonte2 / mag(r2) ** 2) * norm(r2)
    E3 = (usqpez * q_fonte3 / mag(r3) ** 2) * norm(r3)

    Er = E1 + E2 + E3

    arrow(pos=r_obs, color=color.red, axis=fe * Er / 6, shaftwidth=fonte1.radius / 4)
    teta = teta + dteta
