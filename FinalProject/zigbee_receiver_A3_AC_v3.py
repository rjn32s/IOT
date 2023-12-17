import paho.mqtt.client as mqtt_client
import serial
import time
import random


# Enable USB Communication on Actuator 1
ser = serial.Serial('COM5', 9600,timeout=.5)

broker = '192.168.34.10'
port = 1883

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        message = str(msg.payload.decode())
        print("Value = ", message)
        
    
    client.subscribe(topic)
    client.on_message = on_message


def run(topic):
    client = connect_mqtt()
    subscribe(client, topic)
    # client.loop_forever()
    return


# incoming_msg = ''
def sub_mqtt_zigbee():

    interupt = input("If need data of other Sensor - Press Yes or Y:  ")
    # interupt = "Y"
    if(interupt == 'Y' or interupt == "Yes"):
        subnet = int( input("If want data of Nodemcu subnet press 1 else press 0 for Zigbee Subnet:  ") )
        # subnet = 0
        if subnet == 0:
            sen = int(input("Enter the Zigbee number:  "))
            if(sen == 1):
                print("Zigbee 1 value")
                topic = "mqtt/z1"
                run(topic)
            elif(sen == 2):
                print("Zigbee 2 value")
                topic = "mqtt/z2"
                run(topic)
            elif(sen == 3):
                print("Zigbee 3 value")
                topic = "mqtt/z3"
                run(topic)
            else:
                print("No such zigbee exist")
        
        elif subnet == 1:
            sen = int(input("Enter the Nodemcu number:  "))
            if(sen == 1):
                print("Sensor 1 value")
                topic = "mqtt/s1"
                run(topic)
            elif(sen == 2):
                print("Sensor 2 value")
                topic = "mqtt/s2"
                run(topic)
            elif(sen == 3):
                print("Sensor 3 value")
                topic = "mqtt/s3"
                run(topic)
            elif(sen == 4):
                print("Sensor 4 value")
                topic = "mqtt/s4"
                run(topic)
            else:
                print("No such sensor exist")

    

while True:
    incoming = ser.readline().strip()
    message = incoming.decode("utf-8")
    # message = "001" 
    print("Lenthg of message is:", len(message))
    print("Type of message is", type(message))

    if(len(message) == 3):
#       print("In if loop", message)
        if(message[0] == "1"):
            print("Received Light State : On")
        elif(message[0] == "0"):
            print("Received Light State : Off")
        
        # Calling function to
        sub_mqtt_zigbee()

    elif len(message) > 3:
        content = message.split(" ")
        print(content)
        if "z3" in  content[1]:
            print("Received value = {} from Zigbee {}".format(content[2], content[0][-1]))
        
    # choice = input("Want to send some random value from zigbee: ")
# if choice == "Y":
    send_zb_num = random.randint(1, 3)
    val = random.randint(0, 50)
    ser.write(bytes("z3 z" + str(send_zb_num) + " " + str(val), encoding='UTF-8'))

    # For Debug purpose
#     print('Received Data : '+ message)
    # adding 2 seconds time delay
    time.sleep(1)
