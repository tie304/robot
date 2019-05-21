import io

import socket
import time
import sys
import struct
from PIL import Image
import numpy as np
from multiprocessing import Process
from pynput import keyboard


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

current_key = None
# Accept a single connection and make a file-like object out of it
def on_press(key):
    try:
        global current_key
        current_key = key.char
    except AttributeError:
        pass        
def on_release(key):

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# ...or, in a non-blocking fashion:

print('starting sockets')
try:
    while True:
        client, addr = server_socket.accept()
        print(client, "has connected")

        while True:
            if current_key:
                client.send(bytes(current_key, "utf-8"))
                current_key = None
    conn.close()
    print('client disconnected')

finally:
    server_socket.close()
