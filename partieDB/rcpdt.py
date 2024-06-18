import pandas as pd
import paho.mqtt.client as mqtt
import json

message1 = [('sae24/E103/ultra', '{"id": "capteur0", "data": "0"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "1"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "0"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "1"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "0"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "1"}'),
            ('sae24/E103/ultra', '{"id": "capteur0", "data": "0"}')]
# Variable globale pour stocker les messages MQTT
messages = []

# Définir les fonctions de rappel pour différents événements MQTT
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # S'abonner à un sujet après la connexion au broker
    client.subscribe("sae24/+/ultra")

def on_message(client, userdata, msg):
    global messages
    topic = msg.topic
    payload = str(msg.payload.decode("utf-8"))  # Décoder le message en UTF-8
    #print(f"Message reçu sur le sujet {topic} : {payload}")
    # Ajouter le message à la liste
    messages.append((topic, payload))

# Créer un client MQTT
client = mqtt.Client()

# Assigner les fonctions de rappel
client.on_connect = on_connect
client.on_message = on_message

# Configurer le broker MQTT (adresse, port, et éventuellement les identifiants)
broker_address = "192.168.102.200"
broker_port = 1883
username = "Capt1"
password = "a"

# Si le broker nécessite un identifiant et un mot de passe
client.username_pw_set(username, password)

# Se connecter au broker MQTT
client.connect(broker_address, broker_port, 60)

# Boucle pour traiter les messages réseau et les rappels MQTT
client.loop_start()

# Attendre quelques secondes pour recevoir des messages
import time
time.sleep(10)


for topic, payload in messages:
    try:
        #decodage du json du broker 
        data = json.loads(payload)
        print(f"Sujet : {topic}, Données : {data}")
        # teste décriptae de du json
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON pour le message sur le sujet {topic} : {payload}")

# Arrêter la boucle
client.loop_stop()

print(messages)

"""
excel_file = 'matrices_tournees.xlsx'  # Remplacez par le chemin de votre fichier Excelcx
df1 = pd.read_excel(excel_file, sheet_name='AtenuationC1', header=None)
df2 = pd.read_excel(excel_file, sheet_name='AtenuationC2', header=None)
df3 = pd.read_excel(excel_file, sheet_name='AtenuationC3', header=None)

values1 = df1.values.tolist()
values2 = df2.values.tolist()
values3 = df3.values.tolist()

"""