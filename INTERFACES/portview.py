#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color, Port
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
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

light_sensor_01 = ColorSensor(Port.S1)
light_sensor_02 = ColorSensor(Port.S2)
light_sensor_03 = ColorSensor(Port.S3)

medium_A_motor = Motor(Port.A)
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
medium_D_motor = Motor(Port.D)


def start():
    ev3.screen.clear()
    portview_font = Font(size=13)
    ev3.screen.set_font(portview_font)
    ev3.screen.load_image('./IMAGES/display_portview.png')
    while not buttons.pressed(Button.DOWN):
        battery.voltage_text()
        # Sensores
        ev3.screen.draw_text(
            *ports_coordinates[0], text=int(light_sensor_01.reflection()))
        ev3.screen.draw_text(
            *ports_coordinates[1], text=int(light_sensor_02.reflection()))
        ev3.screen.draw_text(
            *ports_coordinates[2], text=int(light_sensor_03.reflection()))

        # Motores
        ev3.screen.draw_text(
            *ports_coordinates[3], text=int(medium_A_motor.angle()))
        ev3.screen.draw_text(
            *ports_coordinates[4], text=int(right_motor.angle()))
        ev3.screen.draw_text(
            *ports_coordinates[5], text=int(left_motor.angle()))
        ev3.screen.draw_text(
            *ports_coordinates[6], text=int(medium_D_motor.angle()))

    ev3.screen.clear()
