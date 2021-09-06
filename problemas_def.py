#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Port
from pybricks.media.ev3dev import Font

# Definição do brick como ev3
ev3 = EV3Brick()

small_font = Font(size=12)

#Código
def teste_de_problemas_motores():
    ev3.screen.set_font(small_font)
    try:
        left_motor = Motor(Port.A)
    except:
        ev3.screen.draw_text(66, 55, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(66, 55, "ok", Color.BLACK, None)

    try:
        left_motor = Motor(Port.B)
    except:
        ev3.screen.draw_text(66, 72, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(66, 72, "ok", Color.BLACK, None)

    try:
        right_motor = Motor(Port.C)
    except:
        ev3.screen.draw_text(66, 89, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(66, 89, "ok", Color.BLACK, None)

    try:
        right_motor = Motor(Port.D)
    except:
        ev3.screen.draw_text(66, 106, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(66, 106, "ok", Color.BLACK, None)

def teste_de_problemas_sensores():
    ev3.screen.set_font(small_font)
    try:
        color_sensor1 = ColorSensor(Port.S1)
    except:
        ev3.screen.draw_text(148, 55, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(148, 55, "ok", Color.BLACK, None)

    try:
        color_sensor2 = ColorSensor(Port.S2)
    except:
        ev3.screen.draw_text(148, 72, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(148, 72, "ok", Color.BLACK, None)

    try:
        color_sensor3 = ColorSensor(Port.S3)
    except:
        ev3.screen.draw_text(148, 89, "none", Color.BLACK, None)
    else:
        ev3.screen.draw_text(148, 89, "ok", Color.BLACK, None)