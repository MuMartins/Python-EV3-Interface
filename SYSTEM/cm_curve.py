#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

# Definição do brick como ev3
ev3 = EV3Brick()

# Iniciando os motores
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Definindo os valores do DriveBase
robot = DriveBase(left_motor, right_motor, wheel_diameter=49.5, axle_track=95)

# Cm sem correção


def cm_no_correction(centimeters):
    millimeter = centimeters * 10
    robot.straight(millimeter)


# Move curva
def move_curve(required_turn):
    # Diametro do giro do robô
    # Todas as medidas convertidas para centimetros
    axle_track = 9.5
    tire_band = 2
    friction_variable = 1.3

    swivel_diameter = (tire_band * friction_variable) + axle_track

    # Graus necessários
    wheel_diameter = 4.95
    spin = 360

    required_degrees = ((swivel_diameter / wheel_diameter)
                        * (required_turn / spin)) * spin

    # Em ação
    print(required_degrees)
    # left_motor.run_angle(360, (-required_degrees),
    #                      then=Stop.HOLD, wait=False)
    # right_motor.run_angle(360, required_degrees,
    #                       then=Stop.HOLD, wait=True)
