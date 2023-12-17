import socket
import time
import numpy as np
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.43.47', 11152))
while True:
    data = sock.recv(8192)
    print(data.decode())
    time.sleep(2)
