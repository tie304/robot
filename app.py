import socket
import time
from pysabertooth import Sabertooth
from models.robot import Robot
from models.camera import Camera
from multiprocessing import Process

PORT = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A105QI4I-if00-port0"


saber = Sabertooth(PORT, baudrate=9600, address=128, timeout=0.1)



robot = Robot(saber)
camera = Camera('test_1', "./data/")





client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.0.0.30", 8000))


button_delay = 0.2




def run_sockets():
    try:

        while True:
            from_server = client_socket.recv(4096)
            char = from_server.decode("utf-8")

            if char == "p":
                print("Stoping robot")
                robot.stop()
                time.sleep(1)
                camera.done()

                exit(0)

            if char == "c":
                robot.stop()
                time.sleep(button_delay)

            if char == "a":
                robot.left()
                camera.set_label('left')
                time.sleep(button_delay)


            elif char == "d":
                robot.right()
                camera.set_label('right')
                time.sleep(button_delay)


            elif char == "w":
                robot.forward()
                camera.set_label('forward')
                time.sleep(button_delay)

            elif char == "s":
                robot.backward()
                time.sleep(button_delay)

            camera.record()

    finally:
        client_socket.close()




def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
        for p in proc:
            p.join()

runInParallel(run_sockets, run_camera)
