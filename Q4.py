"""4. O código seguinte cria dois objetos representando um dipolo (duas cargas iguais com
sinais contrários separados por uma certa distância) orientado ao longo do eixo-y.
Complete o programa para calcular e mostrar (em forma de setas) o campo elétrico
devido ao dipolo em 12 posições de localizações igualmente espaçadas sobre um
círculo de raio 0,5nm no plano xy, centrado sobre o dipolo. """

from vpython import *

scene.width = scene.height = 800
oofpez = 9e9
qe = 1.6e-19
sf = 5e-20

source_01 = sphere(pos=vector(0, 0.1e-9, 0), color=color.red, radius=0.5e-10)
q_01 = +qe

source_02 = sphere(pos=vector(0, -0.1e-9, 0), color=color.red, radius=0.5e-10)
q_02 = -qe

circle_points = 12
radius_circle = 0.5e-9

circle_positions = [vector(radius_circle * cos(2 * pi * i / circle_points), radius_circle * sin(2 * pi * i / circle_points), 0) for i in range(circle_points)]

arrows = []

for pos in circle_positions:
    E = vector(0, 0, 0)
    r1 = pos - source_01.pos
    r2 = pos - source_02.pos

    E += oofpez * q_01 * r1 / mag(r1) ** 3
    E += oofpez * q_02 * r2 / mag(r2) ** 3

    arrows.append(arrow(pos=pos, axis=E * sf, color=color.green))
