import serial
import time
if __name__ == '__main__':
    # Initialialing the serial communication
    ser1 = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser2 = serial.Serial('/dev/ttyACM1', 9600, timeout=1) # Switcher
    opr1 = serial.Serial('/dev/ttyUSB0',9600,timeout =1)# Node MCU 1
    opr2 = serial.Serial('/dev/ttyUSB1',9600,timeout =1)# Node MCU 2
    # Reset the input buffer 
    ser1.reset_input_buffer()
    opr1.reset_input_buffer()
    ser2.reset_input_buffer()
    opr2.reset_input_buffer()
    while True:
        # IF data is avialable
        if ser1.in_waiting > 0 and ser2.in_waiting >0:
            # Read Serial data
            line = ser1.readline().decode('utf-8').rstrip()
            line2 = ser2.readline().decode('utf-8').rstrip()
            #decoded_bytes = float(line[0:len(line)-2].decode("utf-8"))
            #Sensor Value
            #One Human sensor returns 0 , 1
            #One is tempratrue sensor retuns 0 to 9
            
            sensor_value = int(line)
            sensor2_value = int(line2)
            print(f'Current Snesor  1 Value:{sensor_value}')
            print(f'Current Snesor 2  Value:{sensor2_value}')
            if sensor_value == 1:
                # Person is available
                # Check the tempratue of > 5
                if sensor2_value > 5:
                    opr1.write(sensor2_value)
                
            else:
                opr2.write(opr1.write(sensor2_value))
            time.sleep(10)
                
                
                
#                 
#             
#             #print(type()