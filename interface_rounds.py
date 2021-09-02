#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from system_buttons import *

# Definição do brick como ev3
ev3 = EV3Brick()

# # Iniciando os motores
# right_motor = Motor(Port.A)
# left_motor = Motor(Port.D)

# # Drive base (aqui será adicionado tudo referente ao robô, fazendo o calculo automático de giro, milimitros e etc)
# luis = DriveBase(left_motor, right_motor, wheel_diameter=49.5, axle_track=9.5)

# Código
def set_menu():
    round_selecionador = 0
    while True:
        if button_pressed(Button.RIGHT):
            while not button_released(Button.RIGHT):
                wait(10)
            round_selecionador = (round_selecionador + 1) % 4
        
        elif button_pressed(Button.LEFT):
            while not button_released(Button.LEFT):
                wait(10)
            round_selecionador = (round_selecionador - 1) % 4
        
        if round_selecionador == 0:
            ev3.screen.load_image('./IMG_ROUNDS/round_01')
        
        if round_selecionador == 1:
            ev3.screen.load_image('./IMG_ROUNDS/round_02')

        if round_selecionador == 2:
            ev3.screen.load_image('./IMG_ROUNDS/round_03')

        if round_selecionador == 3:
            ev3.screen.load_image('./IMG_ROUNDS/round_04')

        # if button_pressed(Button.CENTER):
        #     if round_selecionador == 0:
        #         ev3.screen.clear()
        #         while True:
        #             if button_pressed(Button.DOWN):
        #                 break
        #             else:
        #                 luis.straight(1000)
        #                 ev3.speaker.beep()

        #     if round_selecionador == 1:
        #         ev3.screen.clear()
        #         while True:
        #             if button_pressed(Button.DOWN):
        #                 break
        #             else:
        #                 luis.straight(-1000)
        #                 ev3.speaker.beep()

        #     if round_selecionador == 2:
        #         ev3.screen.clear()
        #         while True:
        #             if button_pressed(Button.DOWN):
        #                 break
        #             else:
        #                 luis.turn(360)
        #                 ev3.speaker.beep()
            
        #     if round_selecionador == 3:
        #         ev3.screen.clear()
        #         while True:
        #             if button_pressed(Button.DOWN):
        #                 break
        #             else:
        #                 luis.turn(-360)
        #                 ev3.speaker.beep()