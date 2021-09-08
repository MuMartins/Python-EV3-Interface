#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Button, Color, Port
from pybricks.media.ev3dev import Font

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons
import SYSTEM.check_conections as check_conections

# Definição do brick como ev3
ev3 = EV3Brick()


ports_coordinates = [
    [148, 55],  # Port.S1
    [148, 72],  # Port.S2
    [148, 89],  # Port.S3
    [66, 55],   # Port.A
    [66, 72],   # Port.B
    [66, 89],   # Port.C
    [66, 106]   # Port.D
]


def start():
    '''Inicia e gerencia a tela de problemas'''
    ev3.screen.clear()
    problems_font = Font(size=13)
    ev3.screen.set_font(problems_font)
    ev3.screen.load_image('./IMAGES/display_problems.png')
    while not buttons.pressed(Button.DOWN):
        battery.voltage_text()
        # Sensores
        ev3.screen.draw_text(
            *ports_coordinates[0], text=str(check_conections.sensor(Port.S1)))
        ev3.screen.draw_text(
            *ports_coordinates[1], text=str(check_conections.sensor(Port.S2)))
        ev3.screen.draw_text(
            *ports_coordinates[2], text=str(check_conections.sensor(Port.S3)))

        # Motores
        ev3.screen.draw_text(
            *ports_coordinates[3], text=str(check_conections.motor(Port.A)))
        ev3.screen.draw_text(
            *ports_coordinates[4], text=str(check_conections.motor(Port.B)))
        ev3.screen.draw_text(
            *ports_coordinates[5], text=str(check_conections.motor(Port.C)))
        ev3.screen.draw_text(
            *ports_coordinates[6], text=str(check_conections.motor(Port.D)))

    ev3.screen.clear()
