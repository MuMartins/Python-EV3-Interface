#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait

'''
Arquivo responsável pelo controle dos botões do brick
'''

ev3 = EV3Brick()


def released(button: Button):
    '''Retorna se o botão informado está solto'''
    return button not in ev3.buttons.pressed()


def pressed(button: Button):
    '''Retorna se o botão informado está pressionado'''
    return button in ev3.buttons.pressed()


def wait_bumped(button: Button):
    '''Espera até que o botão informado seja pressionado e solto'''
    while not pressed(button):
        wait(10)

    while not released(button):
        wait(10)
