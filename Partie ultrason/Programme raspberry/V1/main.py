import time
import paho.mqtt.client as mqtt
import random
import grovepi
from grovepi import *
import json

## Variables & fonctions ##
led = 3 # Connexion de la LED sur la pin D3
pinMode(led,"OUTPUT") # parametrer la LED comme sortie
digitalWrite(led,0) # Eteindre la LED
grovepi.set_bus("RPI_1") # parametrer le bus I2C pour utiliser le materiel
ultrasonic = 2 # Connexion du capteur ultrason sur la pin D4
seuil = 0
def on_connect(client, userdata, flags, rc): # message lors de la connexion au serveur
    print("Connecté avec le code de retour: " + str(rc))
def publish(topic, message): # Publier la donnée sur le broker MQTT
    print("Valeur publiée: " + message)
    client.publish(topic, message)

#### Initialisation connexion serveur MQTT ####
client = mqtt.Client() # Créer une instance du client
client.username_pw_set("CaptU1", "a") # ID et MDP de connexion
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Attacher les fonctions de callback
client.on_connect = on_connect

# Se connecter au serveur MQTT
while True:
    try:
        client.connect("192.168.102.200", 1883, 60)
    except:
        print("Erreur de connexion au serveur")
        # Clignoter la LED
        for i in range(5):
            digitalWrite(led,1)
            time.sleep(0.1)
            digitalWrite(led,0)
            time.sleep(0.1)

        continue
    else:
        #Executer la suite du code
        break

# Démarrer la boucle réseau
client.loop_start()
#### Fin Initialisation connexion serveur MQTT ####




#### 0 - Initialisation du capteur: Enregistrement du seuil de detection ####
init = True
digitalWrite(led,1) # Allumer la LED
while init: # Tant que le bloque initialisation n'est pas validé
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    if distance != 65535:
        print(distance)
        seuil = distance-40
        print(str("Le seuil enregistré est: ") + str(seuil))
        init = False
    time.sleep(0.2) # ne pas surcharger le bus I2C
digitalWrite(led,0) # Eteindre la LED
#### FIN Initialisation du capteur: Enregistrement du seuil de detection ####


## Main ##
last_val = 0
while True:
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    print("Distance mesurée: " + str(distance))
    if (distance < last_val-15 or distance > last_val+15) and distance < 490: # si la distance change
        if distance < seuil:  ## Faisceau coupé ##
            print(distance)
            data = {
                "id": "capteur1",
                "data": "1"
            }
            publish("sae24/E102/ultra", json.dumps(data)) # Publier la donnée sur le serveur

            last_val = distance # enregistrer la précédante mesure
            digitalWrite(led,1) # Allumer la LED
            time.sleep(0.25)
            digitalWrite(led,0) # Eteindre la LED
        else: ## Faisceau libre ##
            print(distance)
            data = {
                "id": "capteur1",
                "data": "0"
            }
            publish("sae24/E102/ultra", json.dumps(data)) # Publier la donnée sur le serveur

            last_val = distance # enregistrer la précédante mesure
            digitalWrite(led,1) # Allumer la LED
            time.sleep(0.25)
            digitalWrite(led,0) # Eteindre la LED

    time.sleep(0.2) # ne pas surcharger le bus I2C
## Fin Main ##


client.loop_stop() # Arrêter la boucle réseau (deconnexion au serveur MQTT)
