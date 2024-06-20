import pandas as pd
import paho.mqtt.client as mqtt
import json
import time
from collections import deque
import mysql.connector
from datetime import datetime

# Dictionnaire pour stocker les trois dernières valeurs de chaque capteur
# Dictionary to store the last three values of each sensor
capteur_data = {
    "capteur1": deque(maxlen=3),
    "capteur2": deque(maxlen=3),
    "capteur3": deque(maxlen=3)
}

# Liste pour stocker les échantillons
# List to store samples
echantillons = []

# Fonction pour ajouter une nouvelle donnée à la liste des capteurs
# Function to add new data to the sensor list
def add_data(capteur_id, data):
    capteur_data[capteur_id].append(data)
    # Ajouter un nouvel échantillon
    # Add a new sample
    echantillon = {
        "capteur1": list(capteur_data["capteur1"]),
        "capteur2": list(capteur_data["capteur2"]),
        "capteur3": list(capteur_data["capteur3"])
    }
    echantillons.append(echantillon)

# Fonction pour vérifier l'état des capteurs et déterminer la zone
# Function to check the state of the sensors and determine the zone
def determine_zone(capteur_id, capteur_value):
    if capteur_value == "1":
        if capteur_id == "capteur1":
            print("La personne est dans la zone 2")
            send_to_db(3)
        elif capteur_id == "capteur2":
            print("La personne est dans la zone 3")
            send_to_db(5)
        elif capteur_id == "capteur3":
            print("La personne est dans la zone 4")
            send_to_db(7)
    elif capteur_value == "0":
        print(f"{capteur_id} est revenu à 0, aucune mise à jour de la zone.")
        # The sensor has returned to 0, no zone update.

# Fonction pour envoyer les données à la base de données
# Function to send data to the database
def send_to_db(x):
    y = 1
    try:
        conn = mysql.connector.connect(
            host="192.168.102.250",  # Modifier si nécessaire / Modify if necessary
            user="g31",              # Modifier si nécessaire / Modify if necessary
            password="passg31",      # Modifier si nécessaire / Modify if necessary
            database="sae24"
        )
        cursor = conn.cursor()
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        cursor.execute("""
            INSERT INTO Data (X, Y, Date, Time, IDcapteur)
            VALUES (%s, %s, %s, %s, %s)
        """, (x, y, date_str, time_str, x))  # En supposant que IDcapteur correspond à x / Assuming IDcapteur corresponds to x
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Données insérées : X={x}, Y={y}, Date={date_str}, Time={time_str}")
    except mysql.connector.Error as err:
        print(f"Erreur : {err}")

# Définir les fonctions de rappel pour différents événements MQTT
# Define callback functions for different MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # S'abonner à un sujet après la connexion au broker
    # Subscribe to a topic after connecting to the broker
    client.subscribe("sae24/+/ultra")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = str(msg.payload.decode("utf-8"))  # Décoder le message en UTF-8 / Decode the message in UTF-8
    print(f"Message reçu sur le sujet {topic} : {payload}")
    try:
        data = json.loads(payload)
        capteur_id = data['id']
        capteur_value = data['data']
        add_data(capteur_id, capteur_value)
        determine_zone(capteur_id, capteur_value)  # Vérifier la zone après chaque ajout de donnée / Check the zone after each data addition
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON pour le message sur le sujet {topic} : {payload}")

# Créer un client MQTT
# Create an MQTT client
client = mqtt.Client()

# Assigner les fonctions de rappel
# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Configurer le broker MQTT (adresse, port, et éventuellement les identifiants)
# Configure the MQTT broker (address, port, and optionally credentials)
broker_address = "192.168.102.250"
broker_port = 1883
username = "Capt1"
password = "a"

# Si le broker nécessite un identifiant et un mot de passe
# If the broker requires a username and password
client.username_pw_set(username, password)

# Se connecter au broker MQTT
# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Boucle pour traiter les messages réseau et les rappels MQTT
# Loop to handle network messages and MQTT callbacks
client.loop_start()

try:
    # Boucle infinie pour maintenir le programme en cours d'exécution
    # Infinite loop to keep the program running
    while True:
        time.sleep(1)  # Pause to avoid overloading the CPU

except KeyboardInterrupt:
    # Arrêter la boucle MQTT proprement en cas d'interruption par l'utilisateur
    # Properly stop the MQTT loop in case of user interruption
    print("Interruption du programme. Fermeture de la connexion MQTT...")
    client.loop_stop()
    client.disconnect()

# Afficher les trois dernières variations pour chaque capteur dans le même tableau
# Display the last three variations for each sensor in the same table
print("Échantillons collectés avec variations :")
for echantillon in echantillons:
    for capteur_id, values in echantillon.items():
        print(f"Capteur {capteur_id} : dernières variations {values}")
    print("------")
