#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Port
from pybricks.media.ev3dev import Font

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons
import SYSTEM.check_conections as check_conections

# Definição do brick como ev3
ev3 = EV3Brick()

ports_coordinates = [
    [148, 55, 176, 67],  # Port.S1
    [148, 72, 176, 84],  # Port.S2
    [148, 89, 176, 101],  # Port.S3
    [66, 55, 94, 67],   # Port.A
    [66, 72, 94, 84],   # Port.B
    [66, 89, 94, 101],   # Port.C
    [66, 106, 94, 118]   # Port.D
]

last_sensor_value = False
last_motor_value = False

def sensor_connection(sensor_value, sensor_coordinate):
    global last_sensor_value
    problems_font = Font(size=13)
    ev3.screen.set_font(problems_font)
    if sensor_value != last_sensor_value:
        ev3.screen.draw_box(*ports_coordinates[sensor_coordinate], fill=True, color=Color.WHITE)
        ev3.screen.draw_text(ports_coordinates[sensor_coordinate][0],ports_coordinates[sensor_coordinate][1], sensor_value)
        last_sensor_value = sensor_value


def motor_connection(motor_value, motor_coordinate):
    global last_motor_value
    problems_font = Font(size=13)
    ev3.screen.set_font(problems_font)
    if motor_value != last_motor_value:
        ev3.screen.draw_box(*ports_coordinates[motor_coordinate], fill=True, color=Color.WHITE)
        ev3.screen.draw_text(ports_coordinates[motor_coordinate][0], ports_coordinates[motor_coordinate][1], motor_value)
        last_motor_value = motor_value


def start():
    '''Inicia e gerencia a tela de problemas'''
    ev3.screen.clear()
    ev3.screen.load_image('./IMAGES/display_problems.png')
    while not buttons.pressed(Button.DOWN):
        battery.voltage_text()
        # Sensores
        sensor_connection_01 = check_conections.sensor(Port.S1)
        sensor_connection(sensor_connection_01, 0)

        sensor_connection_02 = check_conections.sensor(Port.S2)
        sensor_connection(sensor_connection_02, 1)

        sensor_connection_03 = check_conections.sensor(Port.S3)
        sensor_connection(sensor_connection_03, 2)

        # Motores
        motor_connection_01 = check_conections.motor(Port.A)
        motor_connection(motor_connection_01, 3)

        motor_connection_02 = check_conections.motor(Port.B)
        motor_connection(motor_connection_02, 4)

        motor_connection_03 = check_conections.motor(Port.C)
        motor_connection(motor_connection_03, 5)

        motor_connection_04 = check_conections.motor(Port.D)
        motor_connection(motor_connection_04, 6)

    ev3.screen.clear()
