import grovepi
from grovepi import *
import json
import paho.mqtt.client as mqtt
import time
import sys

## Variables & fonctions ##
led = 3 # Connexion de la LED sur la pin D3
pinMode(led,"OUTPUT") # parametrer la LED comme sortie
digitalWrite(led,0) # Eteindre la LED
grovepi.set_bus("RPI_1") # parametrer le bus I2C pour utiliser le materiel
ultrasonic = 2 # Connexion du capteur ultrason sur la pin D4
seuil = 0

# Attacher les fonctions
client = mqtt.Client() # Créer une instance du client
client.username_pw_set("CaptU1", "a") # ID et MDP de connexion

def mqtt_connect():
    digitalWrite(led,1) # Allumer la LED
    try:
        client.connect("192.168.102.250", 1883)
    except:
        print("Erreur de connexion au serveur")
        sys.exit()
    digitalWrite(led,0) # Eteindre la LED
    print("Connexion au serveur MQTT réussie")
def mqtt_push(message):
    global last_mqtt_msg
    topic = "sae24/E102/ultra"
    print("Publication du message " + str(message))
    try:
        client.publish(topic, json.dumps(message))
    except:
        print("Erreur de l'envoie du message au serveur MQTT")
        mqtt_connect()
    last_mqtt_msg = message
def filtred_value():
    mesures = []
    for i in range(3):
        mesures.append(grovepi.ultrasonicRead(ultrasonic)) # récuperer la distance mesurée
        time.sleep(0.2) # ne pas surcharger le bus I2C
    if max(mesures) - min(mesures) < 4 and max(mesures) < 490:
        # la mesure est correcte
        return round(sum(mesures) / len(mesures))
    else:
        # la mesure est instable
        return 0


### Programme principal ###
mqtt_connect()

## Déterminer la valeur du seuil ##
digitalWrite(led,1) # Allumer la LED
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
digitalWrite(led,0) # Eteindre la LED


while True:
    distance = filtred_value()
    print("Distance: " + str(distance) + "cm")

    if distance < seuil and distance != 0 and last_mqtt_msg.get("data") != "1":
        # nouvelle obstacle détecté
        data = {
            "id": "capteur1",
            "data": "1"
        }
        mqtt_push(data)
        digitalWrite(led,1) # Allumer la LED
    elif distance > seuil and last_mqtt_msg.get("data") != "0":
        # plus d'obstacle
        data = {
            "id": "capteur1",
            "data": "0"
        }
        mqtt_push(data)
        digitalWrite(led,0) # Eteindre la LED

client.disconnect()
### Fin Programme principal ###