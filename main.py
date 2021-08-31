#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Functions
def button_pressed_def(ev3):
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # Now wait for the button to be released.
    while any(ev3.buttons.pressed()):
        pass

    # Return which button was pressed.
    return button

# Write your program here.
menu_interface_selecionador = 1

def main():
    while True: #menu-seleção
        button_pressed = button_pressed_def(ev3)

        # MENU DISPLAY
        if menu_interface_selecionador == 1:
            ev3.screen.load_image('display_menu.png')

        elif menu_interface_selecionador == 2:
            ev3.screen.load_image('display_calibração.png')
        
        elif menu_interface_selecionador == 3:
            ev3.screen.load_image('display_problemas.png')

        elif menu_interface_selecionador == 4:
            ev3.screen.load_image('display_portview.png')

        
        # MENU SELEÇÃO
        if button_pressed == Button.DOWN:
            menu_interface_selecionador += 2
            if menu_interface_selecionador == 5:
                menu_interface_selecionador = 1
            if menu_interface_selecionador == 6:
                menu_interface_selecionador = 2

        elif button_pressed == Button.UP:
            menu_interface_selecionador -= 2
            if menu_interface_selecionador == 0:
                menu_interface_selecionador = 4
            if menu_interface_selecionador < 0:
                menu_interface_selecionador = 3

        elif button_pressed == Button.RIGHT:
            menu_interface_selecionador += 1
            if menu_interface_selecionador == 5:
                menu_interface_selecionador = 1
        
        elif button_pressed == Button.LEFT:
            menu_interface_selecionador -= 1
            if menu_interface_selecionador == 0:
                menu_interface_selecionador = 4

# Run the code
if __name__ == '__main__':
    # Executa nossa função principal
    main()