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

# Drive base (aqui será adicionado tudo referente ao robô, fazendo o calculo automático de giro, milimitros e etc)
robot = DriveBase(left_motor, right_motor, wheel_diameter=49.5, axle_track=95)

# Código 
def round_02(saida_fim):
    move_curva(360)
    ev3.speaker.beep()
    saida_fim = True
    return saida_fim