#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from threading import Thread

import SYSTEM.cm_curve as cm_curve
import SYSTEM.buttons as buttons
import SYSTEM.motor as motor

# Definição do brick como ev3
ev3 = EV3Brick()

# Variável
end_launch = False


def launch():
    global end_launch
    while not end_launch:
        motor.run_time(Port.B, 100, 10, then=Stop.HOLD, wait=False)
        motor.run_time(Port.C, 100, 10, then=Stop.HOLD, wait=True)
        print('ok')
        motor.run_angle(Port.B, 100, 360, then=Stop.HOLD, wait=False)
        motor.run_angle(Port.C, 100, 360, then=Stop.HOLD, wait=True)
        print('ok')
        motor.run_angle(Port.B, 100, -360, then=Stop.HOLD, wait=False)
        motor.run_angle(Port.C, 100, -360, then=Stop.HOLD, wait=True)
        print('ok')
        motor.run_time(Port.B, 100, 10, then=Stop.HOLD, wait=False)
        motor.run_time(Port.C, 100, 10, then=Stop.HOLD, wait=True)
        print('acabou a saida 1')
        wait(10)
        end_launch = True

    if end_launch == True:
        motor.hold(Port.B)
        motor.hold(Port.C)


def start():
    global end_launch
    motor.hold(Port.B)
    motor.hold(Port.C)

    multi = Thread(target=launch, args=())
    multi.start()

    while not end_launch:
        if buttons.pressed(Button.DOWN):
            while not buttons.released(Button.DOWN):
                wait(10)
            end_launch = True
            motor.hold(Port.B)
            motor.hold(Port.C)
