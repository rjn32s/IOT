import network
from esp import espnow
import random
# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)
w0.disconnect()   # For ESP8266

e = espnow.ESPNow()
e.init()
peer = b'\x3c\x71\xbf\xfc\xff\x0c'
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
espList = [esp2,esp3,esp4,esp5]
# MAC address of peer's wifi interface

e.add_peer(peer)
my_peer = [0,1]
next_Assistance = 3#my_peer[random.getrandbits(1)]

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg.decode() =='3':             # msg == None if timeout in irecv()
        print(host, msg)
        e.send(peer,'x'+str(random.getrandbits(3)))
        #e.send(espList[next_Assistance],str(next_Assistance))
        #if msg == b'end':
         #   break