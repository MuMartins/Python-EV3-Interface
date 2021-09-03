#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

from system_buttons import *
from interface_rounds import *
from interface_calibração import *
from interface_problemas import *
from interface_portview import *

# Definição do brick como ev3
ev3 = EV3Brick()

# Código principal
menu_selecionador = [
    # A ordem é X1, Y1, X2, Y2, Preenchimento, Cor
    [3, 27, 85, 75, 1, False, Color.BLACK],     # MENU
    [90, 27, 172, 75, 1, False, Color.BLACK],   # CALIBRACAO
    [3, 78, 85, 126, 1, False, Color.BLACK],    # PROBLEMAS
    [90, 78, 172, 126, 1, False, Color.BLACK]   # PORT_VIEW
]

# Variáveis
menu_selecionador_single = 0
menu_selecionador_single_last = 3

small_font = Font(size=15)

# Função menu
def set_menu_selecionador():
    global menu_selecionador, menu_selecionador_single_last
    if menu_selecionador_single != menu_selecionador_single_last:
        ev3.screen.load_image('./IMG_MENU/display_bottom_battery3.png')
        ev3.screen.draw_box(*menu_selecionador[menu_selecionador_single])
        menu_selecionador_single_last = menu_selecionador_single

def set_current_battery():
    current_battery = ev3.battery.voltage()
    return current_battery

def current_battery_box():
    ev3.screen.set_font(small_font)
    ev3.screen.draw_text(132, 6, set_current_battery(), Color.BLACK, None)

# Code
def main():
    global menu_selecionador_single
    while True:
        set_menu_selecionador()
        current_battery_box()

        # Interface selecionador
        if button_pressed(Button.DOWN):
            while not button_released(Button.DOWN):
                wait(10)
            menu_selecionador_single = (menu_selecionador_single + 2) % 4
        
        elif button_pressed(Button.UP):
            while not button_released(Button.UP):
                wait(10)
            menu_selecionador_single = (menu_selecionador_single - 2) % 4
        
        elif button_pressed(Button.RIGHT):
            while not button_released(Button.RIGHT):
                wait(10)
            menu_selecionador_single = (menu_selecionador_single + 1) % 4
        
        elif button_pressed(Button.LEFT):
            while not button_released(Button.LEFT):
                wait(10)
            menu_selecionador_single = (menu_selecionador_single - 1) % 4
        
        # Interface função
        elif button_pressed(Button.CENTER):
            while not button_released(Button.CENTER):
                wait(10)

            if menu_selecionador_single == 0:
                set_rounds()

            elif menu_selecionador_single == 1:
                set_calibração()
            
            elif menu_selecionador_single == 2:
                set_problemas()
            
            elif menu_selecionador_single == 3:
                set_portview()

if __name__ == '__main__':
    main()