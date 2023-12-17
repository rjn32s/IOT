import socket
import numpy as np
import time
import json
class Homeautomation:
    def __init__(self):
        self.temp = np.random.randint(0,100)
        self.light_intensity = np.random.randint(0,100)
        self.isfanon = 0#np.random.randint(0,2)
        self.isAcon = 0#np.random.randint(0,2)
        self.isLighton = 0#np.random.randint(0,2)
        self.isPerson = np.random.randint(0,2)
        # self.PORT = 11152
        # self.s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.bind((socket.gethostname(), self.PORT))
        # self.s.listen(10)
        # self.conn, self.addr = self.s.accept()
    

    def getStauts(self):
        print(f'IS AC on ? {self.speaktome(self.isfanon)}')
        print(f'is FAN on  {self.speaktome(self.speaktome(self.isfanon))}')
        print(f'Is the person is available ? {self.speaktome(self.isPerson)}')
        print(f'Is light is on ? {self.speaktome(self.isLighton)}')
        print(f'Ciurrent temprature {self.temp}')
        print(f'Ciurrent temprature {self.light_intensity}')




    def tempControl(self):
        if self.isPerson > 0:
            if self.temp <=20:
                self.isAcon == 0
                self.isfanon
            elif self.temp >20 and self.temp <=40:
                self.isfanon = 1
                self.isAcon = 0
            else:
                self.isfanon =0
                self.isAcon = 1
        

        
    def lightControl(self):
        if self.isPerson > 0:
            if self.light_intensity <=50:
                self.isLighton = 1





    def speaktome(self,val):
        if val == 1:
            return 'Yes'
        else:
            return 'No'   
    def statustosend(self,val):
        if val ==1:
            return True
        else:
            return False
    def sendjson(self):
        
        data_set = {
        'fan': self.statustosend(self.isfanon),
        'ac': self.statustosend(self.isAcon),
        'light':self.statustosend(self.isLighton),
        'tv':self.statustosend(self.isPerson),
        'temp':self.temp,
        'lightintensity':self.light_intensity
        }
        json_data = json.dumps(data_set)
        #self.conn.sendall(bytes(json_data,"utf-8"))
        return json_data

if __name__ == "__main__":
    PORT = 11152
    s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.43.217', PORT))
    s.listen(10)
    conn,addr = s.accept()
    while True:
        room1 = Homeautomation()

        print("The Current Status Before Automation:....")
        #room1.getStauts()
        print("Automating>>")
        time.sleep(2)
        room1.lightControl()
        room1.tempControl()
        print("The Current Status After Automation:....")
        room1.getStauts()
        
        conn.sendall(bytes(room1.sendjson(),"utf-8"))
        print(room1.sendjson())
        time.sleep(20)
        print("A Few Monent later....")
