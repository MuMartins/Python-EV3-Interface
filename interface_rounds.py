#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, Stop
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from system_buttons import *
from round_01 import *
from round_02 import *
from round_03 import *
from round_04 import *

from threading import Thread

# Definição do brick como ev3
ev3 = EV3Brick()

# Código
def set_rounds():
    round_selecionador = 0
    while True:
        # Round selecionador
        if button_pressed(Button.RIGHT):
            while not button_released(Button.RIGHT):
                wait(10)
            round_selecionador = (round_selecionador + 1) % 4
        
        elif button_pressed(Button.LEFT):
            while not button_released(Button.LEFT):
                wait(10)
            round_selecionador = (round_selecionador - 1) % 4
        
        # Round display
        if round_selecionador == 0:
            ev3.screen.load_image('./IMG_ROUNDS/round_01')
        
        elif round_selecionador == 1:
            ev3.screen.load_image('./IMG_ROUNDS/round_02')

        elif round_selecionador == 2:
            ev3.screen.load_image('./IMG_ROUNDS/round_03')

        elif round_selecionador == 3:
            ev3.screen.load_image('./IMG_ROUNDS/round_04')

        # Round função
        if button_pressed(Button.CENTER):
            if round_selecionador == 0:
                round_01()
                round_selecionador = (round_selecionador + 1) % 4

            if round_selecionador == 1:
                round_02()
                round_selecionador = (round_selecionador + 1) % 4

            if round_selecionador == 2:
                round_03()
                round_selecionador = (round_selecionador + 1) % 4

            if round_selecionador == 3:
                round_04()
                round_selecionador = (round_selecionador + 1) % 4

            