#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


from main_def import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
while True: #menu-seleção
    menu_interface_selecionador = 1
    while True:
        # MENU DISPLAY
        if menu_interface_selecionador == 1:
            ev3.screen.load_image('display_menu.png')

        if menu_interface_selecionador == 2:
            ev3.screen.load_image('display_calibração.png')
        
        if menu_interface_selecionador == 3:
            ev3.screen.load_image('display_problemas.png')

        if menu_interface_selecionador == 4:
            ev3.screen.load_image('display_portview.png')

        # MENU SELEÇÃO
        if Button.DOWN in ev3.buttons.pressed():
            menu_interface_selecionador += 2
            if menu_interface_selecionador == 5:
                menu_interface_selecionador = 1
            if menu_interface_selecionador == 6:
                menu_interface_selecionador = 2

        if Button.UP in ev3.buttons.pressed():
            menu_interface_selecionador -= 2
            if menu_interface_selecionador == 0:
                menu_interface_selecionador = 4
            if menu_interface_selecionador < 0:
                menu_interface_selecionador = 3

        if Button.RIGHT in ev3.buttons.pressed():
            menu_interface_selecionador += 1
            if menu_interface_selecionador == 5:
                menu_interface_selecionador = 1
        
        if Button.LEFT in ev3.buttons.pressed():
            menu_interface_selecionador -= 1
            if menu_interface_selecionador == 0:
                menu_interface_selecionador = 4
        
        # MENU FUNÇÃO
        if menu_interface_selecionador == 1 and Button.CENTER in ev3.buttons.pressed():
            break
    while True:
        ev3.speaker.beep()