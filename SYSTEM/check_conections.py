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


def light_problems():
    '''Função responsável por mudar a cor dos botões do ev3 dependendo das conexões do brick'''


"""     print(
        ' Sensor S1 {}\n'.format(check_sensor(Port.S1)),
        'Sensor S2 {}\n'.format(check_sensor(Port.S2)),
        'Sensor S3 {}\n'.format(check_sensor(Port.S3)),
        'Motor A {}\n'.format(check_motor(Port.A)),
        'Motor B {}\n'.format(check_motor(Port.B)),
        'Motor C {}\n'.format(check_motor(Port.C)),
        'Motor D {}\n'.format(check_motor(Port.D))
    )
    print('-'*30) """
"""
    if sensor(Port.S1) and sensor(Port.S2) and sensor(Port.S3) and motor(Port.A) and motor(Port.B) and motor(Port.C) and motor(Port.D):
        ev3.light.on(Color.GREEN)
        print('tudo conectado')
    else:
        ev3.light.on(Color.RED)
        print('algo desconectado') """
