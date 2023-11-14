"""6. Adapte o programa anterior em Python para visualizar a trajetória de um elétron num
íon de H2. Use a lei de Coulomb. Todas as cargas no ion tem o mesmo valor (exceto o
sinal), q=1.6 x 10-19C. A massa do elétron é m=9,11 x 10-31kg. A distância entre as
cargas fixas é d=0,535x10-11m. Dados: x0=y0=-2,4x10-10m, vx0=vy0=-2,8x105m, ∆𝑡 = 5x10-
19s. """

from vpython import *

usqpez = 8.99e9
qe = -1.6e-19
me = 9.11e-31
d = 0.535e-11

x0 = -2.4e-10
y0 = -2.4e-10
vx0 = -2.8e5
vy0 = -2.8e5

dt = 5e-19

ion1 = sphere(pos=vector(-d / 2, 0, 0), radius=1e-11, color=color.blue)
ion2 = sphere(pos=vector(d / 2, 0, 0), radius=1e-11, color=color.green)

eletron = sphere(pos=vector(x0, y0, 0), radius=1e-12, color=color.orange, make_trail=True)

eletron.velocidade = vector(vx0, vy0, 0)
eletron.massa = me

scene.userzoom = False
scene.userspin = False
scene.userpan = False
scene.autoscale = False

def calcForca(q1, q2, r):
    F = usqpez * q1 * q2 / r**2
    return F

while True:
    rate(200)

    r1 = eletron.pos - ion1.pos
    r2 = eletron.pos - ion2.pos

    mag_r1 = mag(r1)
    mag_r2 = mag(r2)

    rchap1 = r1 / mag_r1
    rchap2 = r2 / mag_r2

    F1 = calcForca(qe, -qe, mag_r1) * rchap1
    F2 = calcForca(qe, -qe, mag_r2) * rchap2

    F_resultante = F1 + F2

    aceleracao = F_resultante / eletron.massa

    eletron.velocidade = eletron.velocidade + aceleracao * dt
    eletron.pos = eletron.pos + eletron.velocidade * dt
