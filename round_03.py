#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from system_buttons import *
from cm_e_curva import *

# Definição do brick como ev3
ev3 = EV3Brick()

# Iniciando os motores
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Código 
def round_03():
    global saida_abortada
    cm_sem_correção(10)
    saida_abortada = True