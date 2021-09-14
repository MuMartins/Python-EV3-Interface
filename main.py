#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons
import SYSTEM.check_conections as check_conections
import INTERFACES.calibration as calibration
import INTERFACES.menu_launches as menu_launches
import INTERFACES.portview as portview
import INTERFACES.problems as problems

'''
Arquivo principal do brick responsável pelo gerenciamento da interface
'''

# Definição do brick como ev3
ev3 = EV3Brick()

# Código principal
menu_states = [
    # Lista com os valores de X1, Y1, X2, Y2, Preenchimentoe e Cor do selecionador da interface
    [3, 27, 85, 75, 1, False, Color.BLACK],     # MENU
    [90, 27, 172, 75, 1, False, Color.BLACK],   # CALIBRACAO
    [3, 78, 85, 126, 1, False, Color.BLACK],    # PROBLEMAS
    [90, 78, 172, 126, 1, False, Color.BLACK]   # PORT_VIEW
]

# Variáveis
state = 0


def set_state(_state):
    global state, menu_states
    state = _state

    # Coloca a imagem de fundo inicial da interface e desenha o quadrado responsável pela seleção dos estados
    ev3.screen.load_image('./IMAGES/display_main_menu.png')
    ev3.screen.draw_box(*menu_states[state])

    # Mostra o valor atual da bateria e faz a verificação das conexões do brick
    battery.voltage_text()


def main():
    '''Inicia e gerencia a tela principal da interface'''
    global state
    battery.voltage_text()
    check_conections.light_problems()
    set_state(state)
    while True:
        # Verifica as conexões do brick mudando o led para vermelho caso haja algum erro
        check_conections.light_problems()

        # Interface selecionador
        if buttons.pressed(Button.DOWN):
            while not buttons.released(Button.DOWN):
                wait(10)
            state = (state + 2) % 4
            set_state(state)

        if buttons.pressed(Button.UP):
            while not buttons.released(Button.UP):
                wait(10)
            state = (state - 2) % 4
            set_state(state)

        if buttons.pressed(Button.RIGHT):
            while not buttons.released(Button.RIGHT):
                wait(10)
            state = (state + 1) % 4
            set_state(state)

        if buttons.pressed(Button.LEFT):
            while not buttons.released(Button.LEFT):
                wait(10)
            state = (state - 1) % 4
            set_state(state)

        # Interface função
        if buttons.pressed(Button.CENTER):
            while not buttons.released(Button.CENTER):
                wait(10)

            if state == 0:
                menu_launches.start()

            elif state == 1:
                calibration.start()

            elif state == 2:
                problems.start()

            elif state == 3:
                portview.start()


def debug():
    '''Função para debug!'''
    while True:
        check_conections.light_problems()
        wait(1000)


# Estrutura de seleção responsável por executar apenas o arquivo com o nome "main"
if __name__ == '__main__':
    _debug = False
    if _debug:
        debug()
    else:
        try:
            main()
        except Exception as e:
            print(e)
