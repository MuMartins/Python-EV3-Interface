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

# Variável responsável por acabar o round e começar o proximo
saida_fim = False

# Código
def set_rounds():
    round_selecionador = 0
    global saida_fim
    while True:
        # Selecionador
        if button_pressed(Button.RIGHT):
            while not button_released(Button.RIGHT):
                wait(10)
            round_selecionador = (round_selecionador + 1) % 4
        
        elif button_pressed(Button.LEFT):
            while not button_released(Button.LEFT):
                wait(10)
            round_selecionador = (round_selecionador - 1) % 4
        
        # Display e função
        if round_selecionador == 0:
            ev3.screen.load_image('./IMG_ROUNDS/round_01')
            if button_pressed(Button.CENTER):
                Thread(target=round_01(saida_fim)).start()

                while not saida_fim:
                    if button_pressed(Button.DOWN):
                        robot.stop()
                        round_selecionador = (round_selecionador + 1) % 4
                        saida_fim = True
        
        if round_selecionador == 1:
            ev3.screen.load_image('./IMG_ROUNDS/round_02')
            if button_pressed(Button.CENTER):
                Thread(target=round_02(saida_fim)).start()

                while not saida_fim:
                    if button_pressed(Button.DOWN):
                        robot.stop()
                        round_selecionador = (round_selecionador + 1) % 4
                        saida_fim = True

        if round_selecionador == 2:
            ev3.screen.load_image('./IMG_ROUNDS/round_03')
            if button_pressed(Button.CENTER):
                Thread(target=round_03(saida_fim)).start()

                while not saida_fim:
                    if button_pressed(Button.DOWN):
                        robot.stop()
                        round_selecionador = (round_selecionador + 1) % 4
                        saida_fim = True

        if round_selecionador == 3:
            ev3.screen.load_image('./IMG_ROUNDS/round_04')
            if button_pressed(Button.CENTER):
                Thread(target=round_04(saida_fim)).start()

                while not saida_fim:
                    if button_pressed(Button.DOWN):
                        robot.stop()
                        round_selecionador = (round_selecionador + 1) % 4
                        saida_fim = True