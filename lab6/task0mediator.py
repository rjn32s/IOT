
from machine import Pin
import network
import socket
import esp
esp.osdebug(None)
import time
import gc
gc.collect()
import socket

# def make_st():
#     ssid = '6IOT'
#     password = '123456789'
# 
#     station = network.WLAN(network.STA_IF)
# 
#     station.active(True)
#     station.connect(ssid, password)
# 
#     while station.isconnected() == False:
#         pass
# 
#     print('ST')
#     print(station.ifconfig())
#     #time.sleep(10)
#     #station.active(False)
# 
# # def make_ap():
# #     
# #     ssid = 'LAB6IOT'
# #     password = '123456789'
# # 
# #     ap = network.WLAN(network.AP_IF)
# #     ap.active(True)
# #     ap.config(essid=ssid, password=password)
# # 
# #     while ap.active() == False:
# #         pass
# # 
# #     print('AP')
# #     print(ap.ifconfig())
# #     time.sleep(20)
# #     ap.active(False)
# #     time.sleep(5)
# def on_recv():
#     
# 
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('192.168.4.1', 11153))
#     data = sock.recv(8192)
#     #sock.close()
#     return data.decode()
#     #time.sleep(2)
# 
#     
# make_st()

ssid = '6IOT'
password = '123456789'

station = network.WLAN(network.STA_IF)
#time.sleep(5)
station.active(False)

time.sleep(5)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('ST')
print(station.ifconfig())

time.sleep(10)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.4.1', 11153))
data = sock.recv(8192)
sock.close()
data = data.decode()
    #time.sleep(2)


#data = on_recv()
print(data)

    #make_ap()
#time.sleep(5)
station.active(False)

#time.sleep(20)

ssid = 'LAB6IOT'
password = '123456789'
# # 
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
# # 
while ap.active() == False:
    pass
# # 
print('AP')
print(ap.ifconfig())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 11154))
print("1")
sock.listen(10)
print("2")
conn , addr = sock.accept()
print("GOT Connected with :" , addr)
while True:
    conn.sendall(bytes(data,"utf-8"))
    conn.close()
    break

time.sleep(120)
ap.active(False)
#ap.active(False)
#time.sleep(5)
    


#led = Pin(2, Pin.OUT)


