import socket

import numpy as np
import time


PORT = 11153

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((socket.gethostname(), PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

while True:
    # data = conn.recv(8192)
    num = np.random.randint(100)    
    #conn.sendall(bytes(str(np.random.randint(100)),"utf-8"))
    print(conn.recv(8192).decode('UTF-8'))

    time.sleep(2)