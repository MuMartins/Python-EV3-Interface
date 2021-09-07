#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, Stop
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait

import SYSTEM.buttons as buttons
import LAUNCHES.launch_01 as launch_01
import LAUNCHES.launch_02 as launch_02
import LAUNCHES.launch_03 as launch_03
import LAUNCHES.launch_04 as launch_04

# Definição do brick como ev3
ev3 = EV3Brick()


def start():
    launch_selected = 0
    while True:
        # Round selecionador
        if buttons.pressed(Button.RIGHT):
            while not buttons.released(Button.RIGHT):
                wait(10)
            launch_selected = (launch_selected + 1) % 4

        elif buttons.pressed(Button.LEFT):
            while not buttons.released(Button.LEFT):
                wait(10)
            launch_selected = (launch_selected - 1) % 4

        # Round display
        if launch_selected == 0:
            ev3.screen.load_image('./IMAGES/LAUNCHES/01')

        elif launch_selected == 1:
            ev3.screen.load_image('./IMAGES/LAUNCHES/02')

        elif launch_selected == 2:
            ev3.screen.load_image('./IMAGES/LAUNCHES/03')

        elif launch_selected == 3:
            ev3.screen.load_image('./IMAGES/LAUNCHES/04')

        if buttons.pressed(Button.CENTER):
            if launch_selected == 0:
                launch_01.start()
                launch_selected = 1

            elif launch_selected == 1:
                launch_02.start()
                launch_selected = 2

            elif launch_selected == 2:
                launch_03.start()
                launch_selected = 3

            elif launch_selected == 3:
                launch_04.start()