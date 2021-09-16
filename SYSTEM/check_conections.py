#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
import SYSTEM.sensor as sensor
import SYSTEM.motor as motor


'''
Arquivo responsável por checar conexões no brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()


def check_motor(port: Port) -> bool:
    '''Retorna se o motor informado está conectado ou não'''
    return type(motor.angle(port)) == int


def check_sensor(port: Port) -> bool:
    '''Retorna se o sensor informado está conectado ou não'''
    return sensor.reflection(port) >= 0 and sensor.reflection(port) <= 100
