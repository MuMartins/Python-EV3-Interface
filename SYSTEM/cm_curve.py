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
wheel_diameter = 49.5
axle_track = 95
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Cm sem correção


def cm_no_correction(centimeters):
    global robot
    left_motor.position = 0
    right_motor.position = 0
    millimeter = centimeters * 10
    robot.straight(millimeter)


# Move curva
def move_curve(required_turn):
    global robot
    left_motor.position = 0
    right_motor.position = 0
    # This turns 90 deg/sec and not moving 1 second
    robot.drive_time(0, required_turn, 1000)

    # This stops the motor and brakes for accuracy
    robot.stop(Stop.BRAKE)
