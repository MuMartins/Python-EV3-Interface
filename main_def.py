#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick 
from pybricks.parameters import Button
from pybricks.tools import wait

ev3 = EV3Brick()

def button_released(button):
    if button not in ev3.buttons():
        return True
    
    else: 
        return False

def button_pressed(button):
    if button in ev3.buttons():
        return True
    
    else:
        return False

def button_pressed_released(button):
    while not button_pressed(button):
        wait(10)
    
    while not button_released(button):
        wait(10)