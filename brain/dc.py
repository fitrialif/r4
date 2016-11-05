import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Motor1E = 12
Motor1A = 16
Motor1B = 18

GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)


def c1():
    """
    Move the motor 1 clockwise
    """
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)


def cc1():
    """
    Move the motor 1 counter-clockwise
    """
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)


def c2():
    pass


def cc2():
    pass


def stop():
    GPIO.output(Motor1E, GPIO.LOW)


def forward():
    """
    Move the car forward, both wheel-1 & wheel-2 clockwise
    Sleep 1s means both motors move 1s forward
    """
    c1()
    c2()
    time.sleep(1)
    stop()
