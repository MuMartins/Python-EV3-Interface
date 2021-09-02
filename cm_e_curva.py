#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, Stop
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Definição do brick como ev3
ev3 = EV3Brick()

# Iniciando os motores
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Drive base (aqui será adicionado tudo referente ao robô, fazendo o calculo automático de giro, milimitros e etc)
robot = DriveBase(left_motor, right_motor, wheel_diameter=49.5, axle_track=95)

# Cm sem correção
def cm_sem_correção(centimetros):
    milimetros = centimetros * 10
    robot.straight(milimetros)


# Move curva
def move_curva(giro_requerido):
    # Diametro do giro do robô
    entre_rodas = 9.5
    banda_do_pneu = 2
    variavel_de_atrito = 1.3

    diametro_do_giro = (banda_do_pneu * variavel_de_atrito) + entre_rodas

    # Graus necessários
    diametro_do_pneu = 4.95
    rotação = 360

    graus_necessarios = ((diametro_do_giro / diametro_do_pneu) * (giro_requerido / rotação)) * rotação

    # Em ação
    left_motor.run_angle(360, (-graus_necessarios), then=Stop.HOLD, wait=False)
    right_motor.run_angle(360, graus_necessarios, then=Stop.HOLD, wait=True)