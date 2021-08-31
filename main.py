#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


from main_def import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
def main():
    menu_interface_selecionador = 1
    button_pressed = button_pressed_def(ev3)
    menu_display = menu_display_def()
    menu_seleção = menu_seleção_def()
    while True: #menu-seleção
        # MENU DISPLAY
        menu_display()

        # MENU SELEÇÃO
        menu_seleção()

        # MENU FUNÇÃO
        if button_pressed == Button.CENTER:
            menu_função_def()
# Run the code if it's in the same name
if __name__ == '__main__':
    # Execute the code
    main()