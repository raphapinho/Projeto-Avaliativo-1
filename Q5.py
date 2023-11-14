"""5. A listagem do programa a seguir modela o movimento de uma carga (q_pm) sob a
ação de um campo elétrico gerado por outra carga pontual (conforme explicado em
sala de aula e conforme o algoritmo explicado). Adapte o programa para visualizar o
movimento de desta carga sob a ação das cargas de um dipolo (conforme a descrição
no problema 4) """

from vpython import *

usqpez = 9e9
qe = 1.6e-19
fe = 5e-20
E_res=vector(0,0,0) #inicializa o E_res
fonte=sphere(pos=vector(0,0,0), radius=1e-9,
 color=color.red)
pm=sphere(pos=vector(0.5e-8,1.e-8,0), radius=1e-9, color=color.blue,make_trail=True)

dipolo = sphere(pos=vector(0.5e-8,1.e-8,0), radius=1e-9, color=color.green)

v_pm = vector(0, 1e4, 0)

pm.trail = curve(color = color. orange, radius = 1e-11)

tmax=8e-12
q_fonte = +qe
q_pm = -qe
pp_pm=1.7e-27
p_pm=pp_pm*vector(0,5e3,0)
deltat=1e-15
t=0
while t<tmax:
    rate(100)
    r = pm.pos-fonte.pos

    
    rchap=r/mag(r)
    E= (usqpez*q_fonte/mag(r)**2)*rchap
    F = q_pm * E
    p_pm= p_pm + F *deltat
    pm.pos=pm.pos + (p_pm/pp_pm)*deltat
    t = t +deltat 
