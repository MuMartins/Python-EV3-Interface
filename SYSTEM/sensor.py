#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor


def reflection(port: Port) -> int:
    '''
    Retorna a reflectância do sensor de cor na porta especificada.

    port: Porta do sensor de cor.
    '''
    try:
        sensor = ColorSensor(port)
    except OSError:
        return -999

    return sensor.reflection()


def color(port: Port) -> Color:
    '''
    Retorna a cor do sensor de cor na porta especificada.

    port: Porta do sensor de cor.
    '''
    try:
        sensor = ColorSensor(port)
    except OSError:
        return -999

    return sensor.color()


def rgb(port: Port) -> tuple:
    '''
    Retorna o RGB do sensor de cor na porta especificada.

    port: Porta do sensor de cor.
    '''
    try:
        sensor = ColorSensor(port)
    except OSError:
        return -999

    return sensor.rgb()
