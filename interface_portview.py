#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait

from system_buttons import *

# Definição do brick como ev3
ev3 = EV3Brick()

def set_portview():
    ev3.screen.clear()
    while True:
        if button_pressed(Button.DOWN):
            break
        else:
            ev3.screen.draw_box(50,30,90,60)