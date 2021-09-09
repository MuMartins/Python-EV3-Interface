#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

import SYSTEM.cm_curve as cm_curve

# Definição do brick como ev3
ev3 = EV3Brick()

# Iniciando os motores
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


def start():
    cm_curve.cm_no_correction(10)
    cm_curve.move_curve(360)
    print('SAIDA 1 FINALIZADA')
