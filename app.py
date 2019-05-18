import sys, termios, tty, os
import time
from pysabertooth import Sabertooth
from models.robot import Robot

PORT = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A105QI4I-if00-port0"


saber = Sabertooth(PORT, baudrate=9600, address=128, timeout=0.1)



robot = Robot(saber)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.2

while True:
    char = getch()
    char = char.lower()

    if char == "p":
        print("Stoping robot")
        exit(0)

    if char == " ":
        robot.stop()
        time.sleep(button_delay)

    if char == "a":
        robot.left()
        time.sleep(button_delay)

    elif char == "d":
        robot.right()
        time.sleep(button_delay)

    elif char == "w":
        robot.forward()
        time.sleep(button_delay)

    elif char == "s":
        robot.backward()
        time.sleep(button_delay)
