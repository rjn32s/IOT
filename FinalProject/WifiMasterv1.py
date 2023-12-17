import network
from esp import espnow
import json
import time
import random
# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)
w0.disconnect()   # For ESP8266

e = espnow.ESPNow()
e.init()
esp1 = b'\x3c\x71\xbf\xfc\xff\x0c'
esp2 = b'\x60\x01\x94\x5e\x44\x72'
esp3 = b'\x60\x01\x94\x5c\xdb\xef'
esp4 = b'\xbc\xdd\xc2\x9e\x0c\x73'
esp5 = b'\x2c\x3a\xe8\x43\x86\xfb'
  # MAC address of peer's wifi interface
e.add_peer(esp2)
e.add_peer(esp3)
e.add_peer(esp4)
e.add_peer(esp5)

# e.send("Starting...")       # Send to all peers
# for i in range(100):
#     e.send(str(i)*20)
# e.send(b'end')

x = {
  "temp": 0,
  "person": 0,
  "light": 0,
  "mf":0,
}

# convert into JSON:


y = json.dumps(x)
espList = [esp2 , esp3,esp4,esp5]
temp = 0
person =0
light = 0
# Selecting the Random Assistance
Assistance = 0#random.randint(0,2)
print("Random Assitans is :" , Assistance+2)
e.send(espList[Assistance],str(Assistance))
count =0
while count<3:
    
    host , msg = e.irecv()
    if msg:
        val = msg.decode('UTF-8')
        if val[0] =='t':
            print("temp: ",val)
            x['temp'] = int(val[1:])
            count +=1
        if val[0] =='p':
            print("person: ",val)
            x['person'] = int(val[1:])
            count +=1
        if val[0] =='l':
            print("light: ",val)
            x['light'] = int(val[1:])
            count +=1
        if val[0] =='x':
            print("light: ",val)
            x['mf'] = int(val[1:])
            count +=1
y = json.dumps(x)
print(y)

time.sleep(20)
from machine import UART

uart = UART(1, 115200)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1)
for i in range(10):
    uart.write(str(y))
    time.sleep(2)