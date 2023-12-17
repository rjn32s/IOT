try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import time


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('',11581))
s.listen(5)

while True:
    conn , addr = s.accept()
    request = conn.recv(1024)
    #request = request.decode('UTF-8')
    print(request)
    led = Pin(2, Pin.OUT)
    if request.decode('UTF-8') == 'true':
        led.value(0)
    else:
        led.value(1)
#         time.sleep(0.1)
#         led.value(1)
#         time.sleep(0.1)
#         led.value(0)
    #conn.sendall(re)
    conn.close()
    
