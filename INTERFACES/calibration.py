#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons

'''
Arquivo responsável pela calibração dos sensores do brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()


def start():
    '''Inicia e gerencia a tela da calibração'''
    ev3.screen.clear()
    ev3.screen.load_image('./IMAGES/CALIBRATION/display_enter.png')
    while not buttons.pressed(Button.DOWN):
        pass
    
    # Reseta a tela do brick para voltar para o menu principal
    ev3.screen.clear()