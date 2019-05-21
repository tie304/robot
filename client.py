import socket
from models.robot import robot

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.0.0.30", 8000))

#
#     button_delay = 0.2
#
#     while True:
#
#
try:

    while True:
        from_server = client_socket.recv(4096)
        char = from_server.decode("utf-8")

        if char == "p":
            print("Stoping robot")
            robot.stop()
            time.sleep(1)
            #camera.done()

            exit(0)

        if char == " ":
            robot.stop()
            time.sleep(button_delay)

        if char == "a":
            robot.left()
            #camera.set_label('left')
            time.sleep(button_delay)


        elif char == "d":
            robot.right()
            #camera.set_label('right')
            time.sleep(button_delay)


        elif char == "w":
            robot.forward()
            #camera.set_label('forward')
            time.sleep(button_delay)

        elif char == "s":
            robot.backward()
            time.sleep(button_delay)




finally:
    client_socket.close()
