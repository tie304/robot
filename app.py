import time
from pysabertooth import Sabertooth
from models.robot import Robot

PORT = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A105QI4I-if00-port0"


saber = Sabertooth(PORT, baudrate=9600, address=128, timeout=0.1)



robot = Robot(saber)


print("going forward")
robot.forward()
time.sleep(3)
print("Stopping robot")
robot.stop()
time.sleep(3)
print("going backward")
robot.backward()
time.sleep(3)
print("stopping")
robot.stop()
print("turning left")
robot.left()
time.sleep(3)
print("turning right")
robot.right()
