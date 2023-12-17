import paho.mqtt.client as mqtt #import the client1
import time
import random

# We need to change the config file of Raspi by adding "allow_anonymous true" in that file.

############
def on_message(client, userdata, message):
    # print("message received " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
    print("Topic: {} Message received: {}".format(message.topic, str(message.payload.decode("utf-8"))) )
########################################

broker_address="192.168.34.10" 

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

topics = [ "sensor_data", "mqtt/s1", "mqtt/s2", "mqtt/s3", "mqtt/s4", "mqtt/z1", "mqtt/z2", "mqtt/z3"]

# import datetime
# endTime = datetime.datetime.now() + datetime.timedelta(minutes=15)
# while True:
#   if datetime.datetime.now() >= endTime:

t_end = time.time() + 60 * 5    # Run while loop for 5 minutes
while time.time() < t_end:

    for t in topics:
        print("Subscribing to topic :- ", t)
        client.subscribe(t)
        print("Publishing message to topic :-", t)
        # s1 = str(random.randint(0, 1))
        # s2 = str(random.randint(0, 1))
        # s3 = str(random.randint(0, 1))
        # sensor_values = [s1, s2, s3]
        val = random.randint(0, 90)
        client.publish(t, random.randint(0, val))
        time.sleep(10) # wait 10 second

client.loop_stop() #stop the loop