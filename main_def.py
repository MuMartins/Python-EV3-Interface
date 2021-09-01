#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick 
from pybricks.parameters import Button
from pybricks.tools import wait

ev3 = EV3Brick()

def button_released(button):
    return button not in ev3.buttons.pressed()

def button_pressed(button):
    return button in ev3.buttons.pressed()

def wait_button_bumped(button):
    while not button_pressed(button):
        wait(10)
    
    while not button_released(button):
        wait(10)    


def menu_rounds():
    ev3.screen.load_image('./IMG_ROUNDS/round_01.png')
    if button_pressed(Button.CENTER):
        ev3.speaker.beep()