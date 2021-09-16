#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Port
from pybricks.media.ev3dev import Font

import SYSTEM.battery as battery
import SYSTEM.buttons as buttons
import SYSTEM.check_conections as check_conections


'''
Arquivo responsável por identificar e mostrar problemas nas conexões do brick
'''

# Definição do brick como ev3
ev3 = EV3Brick()

ports_coordinates = [
    # Lista com os valores de X1, Y1, X2, Y2 de cada uma das conexões do brick
    [148, 55, 176, 67],   # Port.S1
    [148, 72, 176, 84],   # Port.S2
    [148, 89, 176, 101],  # Port.S3
    [66, 55, 94, 67],     # Port.A
    [66, 72, 94, 84],     # Port.B
    [66, 89, 94, 101],    # Port.C
    [66, 106, 94, 118]    # Port.D
]


def sensor_connection(sensor_value, sensor_coordinate):
    '''Função responsável por atualizar o texto referente às conexões dos sensores'''
    # Define o tamanho da fonte do texto que será mostrado na tela do brick
    problems_font = Font(size=13)
    ev3.screen.set_font(problems_font)

    # Responsável por atualizar o texto mostrando a leitura dos sensores na tela do brick
    ev3.screen.draw_box(
        *ports_coordinates[sensor_coordinate], fill=True, color=Color.WHITE)
    ev3.screen.draw_text(
        ports_coordinates[sensor_coordinate][0], ports_coordinates[sensor_coordinate][1], sensor_value)


def motor_connection(motor_value, motor_coordinate):
    '''Função responsável por atualizar o texto referente às conexões dos motores'''
    # Define o tamanho da fonte do texto que será mostrado na tela do brick
    problems_font = Font(size=13)
    ev3.screen.set_font(problems_font)

    # Responsável por atualizar o texto mostrando a leitura dos motores na tela do brick
    ev3.screen.draw_box(
        *ports_coordinates[motor_coordinate], fill=True, color=Color.WHITE)
    ev3.screen.draw_text(
        ports_coordinates[motor_coordinate][0], ports_coordinates[motor_coordinate][1], motor_value)


def start():
    '''Inicia e gerencia a tela de problemas'''
    ev3.screen.clear()
    ev3.screen.load_image('./IMAGES/display_problems.png')
    while not buttons.pressed(Button.DOWN):
        # Mostra o valor atual da bateria
        battery.voltage_text()

        # Sensores
        '''Inicia a verificação das conexões dos sensores'''
        sensor_connection_01 = check_conections.check_sensor(Port.S1)
        sensor_connection(sensor_connection_01, 0)

        sensor_connection_02 = check_conections.check_sensor(Port.S2)
        sensor_connection(sensor_connection_02, 1)

        sensor_connection_03 = check_conections.check_sensor(Port.S3)
        sensor_connection(sensor_connection_03, 2)

        # Motores
        '''Inicia a verificação das conexões dos motores'''
        motor_connection_01 = check_conections.check_motor(Port.A)
        motor_connection(motor_connection_01, 3)

        motor_connection_02 = check_conections.check_motor(Port.B)
        motor_connection(motor_connection_02, 4)

        motor_connection_03 = check_conections.check_motor(Port.C)
        motor_connection(motor_connection_03, 5)

        motor_connection_04 = check_conections.check_motor(Port.D)
        motor_connection(motor_connection_04, 6)

    # Reseta a tela do brick para voltar para o menu principal
    ev3.screen.clear()
