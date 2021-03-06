#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.media.ev3dev import Font

'''
Arquivo responsável pelos controles de bateria
'''

ev3 = EV3Brick()


def voltage():
    '''Retorna a tensão atual da bateria'''
    return ev3.battery.voltage()


def voltage_text():
    '''Retorna o texto mostrando a tensão atual da bateria'''
    battery_font = Font(size=15)
    ev3.screen.set_font(battery_font)
    ev3.screen.draw_box(130, 6, 169, 21, fill=True, color=Color.WHITE)
    ev3.screen.draw_text(132, 6, voltage())
