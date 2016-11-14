import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Motor1E = 12
Motor1A = 16
Motor1B = 18

GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)

Motor2E = 22
Motor2A = 24
Motor2B = 26

GPIO.setup(Motor2E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)


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
    """
    Move the motor 2 clcockwise
    """
    GPIO.output(Motor2E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)


def cc2():
    """
    Move the motor 2 counter-clockwise
    """
    GPIO.output(Motor2E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)


def stop1():
    GPIO.output(Motor1E, GPIO.LOW)


def stop2():
    GPIO.output(Motor2E, GPIO.LOW)


def stop():
    stop1()
    stop2()


def forward():
    """
    Move the car forward, both wheel-1 & wheel-2 clockwise
    """
    c1()
    c2()
    time.sleep(1)


def backward():
    """
    Move the car backward, both wheel-1 & wheel-2 counter-clockwise
    """
    cc1()
    cc2()
    time.sleep(1)

def left():
    """
    Steer the car left, wheel-1 stop, wheel-2 clockwise
    """
    stop1()
    c2()
    time.sleep(1)


def right():
    """
    Steer the car right, wheel-1 clockwise, wheel-2 stop
    """
    c1()
    stop2()
    time.sleep(1)
