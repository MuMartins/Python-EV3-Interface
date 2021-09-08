#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color, Port
from pybricks.media.ev3dev import Font

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons
import SYSTEM.check_portview as check_portview

# Definição do brick como ev3
ev3 = EV3Brick()

ports_coordinates = [
    [148, 40],  # Port.S1
    [148, 57],  # Port.S2
    [148, 74],  # Port.S3
    [66, 40],   # Port.A
    [66, 57],   # Port.B
    [66, 74],   # Port.C
    [66, 91]   # Port.D
]


def start():
    ev3.screen.clear()
    portview_font = Font(size=13)
    ev3.screen.set_font(portview_font)
    ev3.screen.load_image('./IMAGES/display_portview.png')
    while not buttons.pressed(Button.DOWN):
        battery.voltage_text()
        # Sensores
        ev3.screen.draw_text(
            *ports_coordinates[0], text=int(check_portview.sensor(Port.S1)))
        ev3.screen.draw_text(
            *ports_coordinates[1], text=int(check_portview.sensor(Port.S2)))
        ev3.screen.draw_text(
            *ports_coordinates[2], text=int(check_portview.sensor(Port.S3)))

        # Motores
        ev3.screen.draw_text(
            *ports_coordinates[3], text=int(check_portview.motor(Port.A)))
        ev3.screen.draw_text(
            *ports_coordinates[4], text=int(check_portview.motor(Port.B)))
        ev3.screen.draw_text(
            *ports_coordinates[5], text=int(check_portview.motor(Port.C)))
        ev3.screen.draw_text(
            *ports_coordinates[6], text=int(check_portview.motor(Port.D)))

    ev3.screen.clear()
