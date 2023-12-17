import socket

import numpy as np


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.4.1', 11154))
data = sock.recv(8192)
sock.close()
data = data.decode()
print(data)

# Creating Json




# while True:
#     # data = conn.recv(8192)
#     num = np.random.randint(100)    
#     data_set = {
#     'fan': True,
#     'ac': False,
#     'light':True,
#     'tv':False,
#     'temp':np.random.randint(100)

#     }
#     json_data = json.dumps(data_set)
#     #conn.sendall(bytes(str(np.random.randint(100)),"utf-8"))
#     conn.sendall(bytes(json_data,"utf-8"))
#     print(bytes(json_data,"utf-8"))
#     time.sleep(2)