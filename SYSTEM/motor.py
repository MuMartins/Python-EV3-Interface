#!/usr/bin/env pybricks-micropython
# Importação dos módulos utilizados
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase


def speed(port: Port) -> int:
    """
    Função que retorna a velocidade do motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    return motor.speed()


def angle(port: Port) -> int:
    """
    Função que retorna o ângulo do motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    return motor.angle()


def reset_angle(port: Port, angle: int = 0) -> None:
    """
    Função que reseta o ângulo do motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.reset_angle(angle)


def stop(port: Port) -> None:
    """
    Função que para o motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.stop()


def brake(port: Port) -> None:
    """
    Função que segura o motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.brake()


def hold(port: Port) -> None:
    """
    Função que trava o motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.hold()


def run(port: Port, speed, time, then=Stop.HOLD, wait=True) -> None:
    """
    Função que executa o motor.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.run(speed, time, then, wait)


def run_time(port: Port, speed, time, then=Stop.HOLD, wait=True) -> None:
    """
    Função que executa o motor por um tempo específico.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.run_time(speed, time, then, wait)


def run_angle(port: Port, speed, target_angle, then=Stop.HOLD, wait=True) -> None:
    """
    Função que executa o motor por um ângulo específico.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.run_angle(speed, target_angle, then, wait)


def run_target(port: Port, speed, target_angle, then=Stop.HOLD, wait=True) -> None:
    """
    Função que executa o motor até uma posição específica.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.run_target(speed, target_position, then, wait)


def run_until_stalled(port: Port, speed, then=Stop.HOLD, wait=True) -> None:
    """
    Função que executa o motor até que ele fique parado.
    """

    try:
        motor = Motor(port)
    except OSError:
        return None

    motor.run_until_stalled(speed, then, wait)
