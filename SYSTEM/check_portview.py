#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port


'''
Arquivo responsável por checar os valores das portas no brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()


def motor(port):
    '''Retorna o valor em que está sendo lido no motor'''
    motor = Motor(port)
    motor.reset_angle(0)
    while True:
        return motor.angle()


def sensor(port):
    '''Retorna o valor em que está sendo lido no sensor'''
    color_sensor = ColorSensor(port)
    # gyro_sensor = GyroSensor(port)
    # gyro_sensor.reset_angle(0)
    while True:
        return color_sensor.reflection()
    # gyro_sensor.angle()
