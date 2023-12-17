import time
import paho.mqtt.client as paho
from paho import mqtt
from datetime import datetime
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv31)
client.on_connect = on_connect

# enable TLS for secure connection
#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
#client.username_pw_set("rjn32s", "pahoMQTT1")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("192.168.34.10")

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
#client.subscribe("mqtt/sensor_data", qos=1)


########################################################### Take Data From UART############
import serial
ser=serial.Serial("COM7",115200)





while True:
    readedText = ser.readline()
    print(readedText.decode('UTF-8'))
    client.publish("mqtt/sensor_data", payload=readedText.decode("UTF-8"), qos=1)
    with open("log.csv ","a") as log:
        timestamp = datetime.now()
        data = readedText.decode("UTF-8")
        log.write("{0},{1}\n".format(str(timestamp),data))
    
    time.sleep(10)







###################################################### Publish to the mqtt/sensor_data##############










# a single publish, this can also be done in loops, etc.


# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()
ser.close()
