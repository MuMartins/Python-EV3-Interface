#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# from threading import Thread
import multiprocessing
from time import sleep

import SYSTEM.cm_curve as cm_curve
import SYSTEM.motor as motor
import SYSTEM.buttons as buttons

# Definição do brick como ev3
ev3 = EV3Brick()

end_launch = False


def launch():
    global end_launch
    print('inicio da saida')
    while not end_launch:
        print('rodando a saida')
        sleep(1)

        # motor.reset_angle(Port.B)
        # motor.reset_angle(Port.C)
        # motor.run_angle(Port.B, speed=100, target_angle=10000, wait=False)
        # motor.run_angle(Port.C, speed=100, target_angle=10000, wait=True)

    print('SAIDA 1 FINALIZADA')
    end_launch = True


def start():
    global end_launch
    # a = Thread(target=launch)
    # a.start()
    a = multiprocessing.Process(target=launch, args=())
    a.start()
    while not end_launch:
        if buttons.pressed(Button.DOWN):
            print('SAÍDA 1 FINALIZADA NA FORÇA')
            end_launch = True
