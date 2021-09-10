#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port


'''
Arquivo responsável por checar conexões no brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()


def motor(port: Port) -> bool:
    '''Retorna se o motor informado está conectado ou não'''
    try:
        motor = Motor(port)
        return True
    except:
        return False


def sensor(port: Port) -> bool:
    '''Retorna se o sensor informado está conectado ou não'''
    try:
        color_sensor = ColorSensor(port)
    except:
        try:
            gyro_sensor = GyroSensor(port)
        except:
            return False
    return True


def light_problems():
    '''Função responsável por mudar a cor dos botões do ev3 dependendo das conexões do brick'''
    if sensor(Port.S1) and sensor(Port.S2) and sensor(Port.S3) and motor(Port.A) and motor(Port.B) and motor(Port.C) and motor(Port.D) == False:
        ev3.light.on(Color.RED)
    else:
        ev3.light.on(Color.GREEN)