import time
from socket import *
from numpy import byte
sock = socket(AF_INET, SOCK_DGRAM)
addr = ("192.168.43.47", 12000)
while True:  
    sock.sendto(str.encode("Hell"), addr)
    try:
        data, server = sock.recvfrom(1024)
        print(data.decode())  
    except timeout:
        print('REQUEST TIMED OUT')