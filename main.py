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
battery = ev3.battery.voltage()

# Write your program here.
screen.clear() #reseta a tela do ev3
menu_interface_selecionador = 1

while True: #menu-seleção
    # MENU DISPLAY
    if menu_interface_selecionador == 1:
        screen.load_image(display_menu.png)

    elif menu_interface_selecionador == 2:
        screen.load_image(display_calibração.png)
    
    elif menu_interface_selecionador == 3:
        screen.load_image(display_problemas.png)

    elif menu_interface_selecionador == 4:
        screen.load_image(display_portview.png)

    
    # MENU SELEÇÃO
    if button.DOWN in ev3.buttons.pressed():
        menu_interface_selecionador += 2
        if menu_interface_selecionador == 5:
            menu_interface_selecionador = 1
        if menu_interface_selecionador == 6:
            menu_interface_selecionador = 2

    elif button.UP in ev3.buttons.pressed():
        menu_interface_selecionador -= 2
        if menu_interface_selecionador == 0:
            menu_interface_selecionador = 4
        if menu_interface_selecionador == -1:
            menu_interface_selecionador = 3

    elif button.RIGHT in ev3.buttons.pressed():
        menu_interface_selecionador += 1
        if menu_interface_selecionador == 5:
            menu_interface_selecionador = 1
    
    elif button.LEFT in ev3.buttons.pressed():
        menu_interface_selecionador -= 1
        if menu_interface_selecionador == 0:
            menu_interface_selecionador = 4




# while True: #menu-main
#     screen.clear() #reseta a tela do ev3
#     menu_interface_selecionador = 1
#     while True: #menu-funções-01
#         while True: #menu-seleção
#             # MENU DISPLAY
#             if menu_interface_selecionador == 1:
#                 screen.load_image(display_menu.png)

#             elif menu_interface_selecionador == 2:
#                 screen.load_image(display_calibração.png)
            
#             elif menu_interface_selecionador == 3:
#                 screen.load_image(display_problemas.png)

#             elif menu_interface_selecionador == 4:
#                 screen.load_image(display_portview.png)

            
#             # MENU SELEÇÃO
#             if button.DOWN in ev3.buttons.pressed():
#                 menu_interface_selecionador += 2
#                 if menu_interface_selecionador == 5:
#                     menu_interface_selecionador = 1
#                 if menu_interface_selecionador == 6:
#                     menu_interface_selecionador = 2

#             elif button.UP in ev3.buttons.pressed():
#                 menu_interface_selecionador -= 2
#                 if menu_interface_selecionador == 0:
#                     menu_interface_selecionador = 4
#                 if menu_interface_selecionador == -1:
#                     menu_interface_selecionador = 3

#             elif button.RIGHT in ev3.buttons.pressed():
#                 menu_interface_selecionador += 1
#                 if menu_interface_selecionador == 5:
#                     menu_interface_selecionador = 1
            
#             elif button.LEFT in ev3.buttons.pressed():
#                 menu_interface_selecionador -= 1
#                 if menu_interface_selecionador == 0:
#                     menu_interface_selecionador = 4
#         while True: #menu-funções

#     while True: #menu-funções-02