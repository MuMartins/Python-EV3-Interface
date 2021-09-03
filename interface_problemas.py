#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.media.ev3dev import Font

from system_buttons import *

# Definição do brick como ev3
ev3 = EV3Brick()

small_font = Font(size=15)

# Código
def set_current_battery():
    current_battery = ev3.battery.voltage()
    return current_battery

def current_battery_text():
    ev3.screen.set_font(small_font)
    ev3.screen.draw_text(132, 6, set_current_battery(), Color.BLACK, None)

def set_problemas():
    while True:
        if button_pressed(Button.DOWN):
            break
        else:
            ev3.screen.load_image('./IMG_PROBLEMAS/display_problemas4.png')
            current_battery_text()