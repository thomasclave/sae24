import grovepi
from grovepi import *
import json
import paho.mqtt.client as mqtt
import time
import sys

## Variables & functions ##
led = 3 # Connecting the LED to pin D3
pinMode(led,"OUTPUT") # set the LED as an output
digitalWrite(led,0) # Switching off the LED
grovepi.set_bus("RPI_1") # Set up the I2C bus to use the hardware
ultrasonic = 2 # Connecting the ultrasonic sensor to pin D4
seuil = 0

# Attach functions
client = mqtt.Client() # Create an instance of the client
client.username_pw_set("CaptU1", "a") # login and password

def mqtt_connect():
    digitalWrite(led,1) # Switch on LED
    try:
        client.connect("192.168.102.250", 1883)
    except:
        print("Erreur de connexion au serveur")
        sys.exit()
    digitalWrite(led,0) # Switching off the LED
    print("Connexion au serveur MQTT réussie")
def mqtt_push(message):
    global last_mqtt_msg
    topic = "sae24/E102/ultra"
    print("Publication du message " + str(message))
    try:
        client.publish(topic, json.dumps(message)) # sends the message to the MQTT server
    except:
        print("Erreur de l'envoie du message au serveur MQTT")
        mqtt_connect()
    last_mqtt_msg = message
def filtred_value():
    mesures = []
    i = 0
    while i < 3:
        distance = grovepi.ultrasonicRead(ultrasonic) # take my measurement
        if distance != 65535:
            mesures.append(distance) # recording the masure in the table
            i = i+1
        time.sleep(0.2) # do not overload the I2C bus
    if max(mesures) - min(mesures) < 4 and max(mesures) < 500:
        # the measurement is correct
        return round(sum(mesures) / len(mesures))
    else:
        # the measurement is unstable
        return 0


### Main programmel ###
mqtt_connect()

## Determining the threshold value ##
digitalWrite(led,1) # Switch on LED
seuil = 0
while seuil <= 10:
    seuil = filtred_value() - 5
    print("Seuil en cours d'enregistrement: " + str(seuil))
print("Le seuil est enregistré à: " + str(seuil) + "cm")
data = {
    "id": "capteur1",
    "data": "0"
}
mqtt_push(data)
digitalWrite(led,0) # Switching off the LED


while True:
    distance = filtred_value()
    print("Distance: " + str(distance) + "cm")

    if distance < seuil and distance != 0 and last_mqtt_msg.get("data") != "1":
        # new obstacle detected
        data = {
            "id": "capteur1",
            "data": "1"
        }
        mqtt_push(data)
        digitalWrite(led,1) # Switch on LED
    elif distance > seuil and last_mqtt_msg.get("data") != "0":
        # no more obstacles
        data = {
            "id": "capteur1",
            "data": "0"
        }
        mqtt_push(data)
        digitalWrite(led,0) # Switching off the LED

client.disconnect()
### End Main programme ###