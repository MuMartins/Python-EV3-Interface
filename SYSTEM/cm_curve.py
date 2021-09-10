#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

'''
Arquivo responsável pelos blocos de centimetros e curva
'''

# Definição do brick como ev3
ev3 = EV3Brick()

# Definição das portas do brick
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Definindo o DriveBase (em milimetros)
wheel_diameter = 49.5
axle_track = 95
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Definindo o bloco que converte centimetros para milimetros na hora andar com o robô
def cm_no_correction(centimeters):
    global robot
    # Reseta o valor dos dois motores grandes para trazer mais precisão
    left_motor.position = 0
    right_motor.position = 0

    # Em ação
    millimeter = centimeters * 10
    robot.straight(millimeter)
    
    # Força os motores a parar para trazer mais precisão 
    robot.stop(Stop.BRAKE)


# Definindo o bloco que converte o giro requerido para o eixo do robô, fazendo-o girar precisamente
def move_curve(required_turn):
    global robot
    # Reseta o valor dos dois motores grandes para trazer mais precisão
    left_motor.position = 0
    right_motor.position = 0

    '''MUDAR E COMEÇAR A USAR GIROSCOPIO TA TUDO DANDO ERRADO'''
    # Isso gira 90 graus/segundo sem mover por 1 segundo
    robot.drive_time(0, required_turn, 1000)

    # Força os motores a parar para trazer mais precisão 
    robot.stop(Stop.BRAKE)
