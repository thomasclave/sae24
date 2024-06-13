import time
import paho.mqtt.client as mqtt
import random
import grovepi
from grovepi import *

## Variables ##
led = 3 # Connexion de la LED sur la pin D3
pinMode(led,"OUTPUT") # parametrer la LED comme sortie
digitalWrite(led,0) # Eteindre la LED
grovepi.set_bus("RPI_1") # parametrer le bus I2C pour utiliser le materiel
ultrasonic = 2 # Connexion du capteur ultrason sur la pin D4
seuil = 0


## Initialisation connexion serveur MQTT ##
def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code de retour: " + str(rc))

def on_publish(client, userdata, mid):
    print("Message publié avec l'ID: " + str(mid))

client = mqtt.Client() # Créer une instance du client
client.username_pw_set("CaptU1", "mosquitto") # ID et MDP de connexion
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Attacher les fonctions de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Se connecter au serveur MQTT
client.connect("192.168.102.200", 1883, 60)

# Démarrer la boucle réseau
client.loop_start()

## Fin Initialisation connexion serveur MQTT ##


## 0 - Initialisation du capteur: Enregistrement du seuil de detection ##
init = True
digitalWrite(led,1) # Allumer la LED
while init: # Tant que le bloque initialisation n'est pas validé
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    if distance != 65535:
        print(distance)
        seuil = distance-40
        print(str("Le seuil enregistré est: ") + str(seuil))
        init = False
    time.sleep(0.1) # ne pas surcharger le bus I2C
digitalWrite(led,0) # Eteindre la LED
## FIN Initialisation du capteur: Enregistrement du seuil de detection ##


## Main ##
last_val = 0
while True:
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    if distance < seuil and (distance < last_val-15 or distance > last_val+15) and distance < 500:
        print(distance)

        # Publier la donnée sur le serveur
        client.publish("sae24/E102/ultra", "id:capteur1 data:1", qos=0) # Obstacle
        print("1")

        last_val = distance # enregistrer le nouveau seuil
        digitalWrite(led,1) # Allumer la LED
        time.sleep(0.25)
        digitalWrite(led,0) # Eteindre la LED
    elif (distance < last_val-15 or distance > last_val+15) and distance < 500:
        ## pas d'ostacle ##
        # Publier la donnée sur le serveur
        client.publish("sae24/E102/ultra", "id:capteur1 data:0", qos=0)
        print(distance)
        print("0")
        last_val = distance # enregistrer le nouveau seuil

    time.sleep(0.1) # ne pas surcharger le bus I2C
## Fin Main ##


client.loop_stop() # Arrêter la boucle réseau (deconnexion au serveur MQTT)
