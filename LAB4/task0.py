

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'iii'
password = 'qwertyuio'

station = network.WLAN(network.STA_IF)

station.active(True)
for i in station.scan():
    for j in i:
        print(j)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#led = Pin(2, Pin.OUT)

from machine import UART
import time
uart = UART(0, 9600)                        
uart.init(9600, bits=8, parity=None, stop=1)

time.sleep(10)
count = 0
while True:
    uart.write('abc')
    time.sleep(0.1)
    count +=1
    print('.')
    if count ==50:
        break


