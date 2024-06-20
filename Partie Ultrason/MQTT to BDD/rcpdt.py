import paho.mqtt.client as mqtt
import json
import time
import mysql.connector
from datetime import datetime
from collections import deque

# Variable globale pour stocker l'historique des zones
# Global variable to store the zone history
zone_history = deque(maxlen=2)

# Fonction pour vérifier l'état des capteurs et déterminer la zone
# Function to check the state of the sensors and determine the zone
def determine_zone(capteur_id, capteur_value):
    global zone_history

    # Déterminer la zone en fonction du capteur
    # Determine the zone based on the sensor
    zone = None
    if capteur_value == "1":
        if capteur_id == "capteur1":
            zone = 3
        elif capteur_id == "capteur2":
            zone = 5
        elif capteur_id == "capteur3":
            zone = 7
    
    if zone is not None:
        # Ajouter la nouvelle zone à l'historique
        # Add the new zone to the history
        zone_history.append(zone)

        # Vérifier si la personne a fait demi-tour
        # Check if the person has turned back
        if len(zone_history) == 2 and zone_history[0] == zone_history[1]:
            print(f"La personne est revenue dans la zone précédente: Zone {zone - 2}")
            send_to_db(zone - 2)
            zone_history.clear()  # Réinitialiser l'historique après détection de demi-tour / Reset history after detecting turn back
        else:
            print(f"La personne est dans la zone {zone}")
            send_to_db(zone)
    
    if capteur_value == "0":
        print(f"{capteur_id} est revenu à 0, aucune mise à jour de la zone.")
        # The sensor has returned to 0, no zone update.

# Fonction pour envoyer les données à la base de données
# Function to send data to the database
def send_to_db(x):
    y = 1
    try:
        conn = mysql.connector.connect(
            host="192.168.102.250",  
            user="g31",              
            password="passg31",      
            database="sae24"
        )
        cursor = conn.cursor()
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        cursor.execute("""
            INSERT INTO Data (X, Y, Date, Time, TypeCapt, NomSalle)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (x, y, date_str, time_str, "Ultrason", "E102"))  # En supposant que IDcapteur correspond à x / Assuming IDcapteur corresponds to x
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Données insérées : X={x}, Y={y}, Date={date_str}, Time={time_str}")
    except mysql.connector.Error as err:
        print(f"Erreur : {err}")

# Fonction pour envoyer la position initiale dans la base de données
# Function to send initial position to the database
def send_initial_position():
    print("Envoi de la position initiale: Zone 1")
    send_to_db(1)

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
username = "CaptU1"
password = "a"

# Si le broker nécessite un identifiant et un mot de passe
# If the broker requires a username and password
client.username_pw_set(username, password)

# Se connecter au broker MQTT
# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Envoi de la position initiale au démarrage
# Send the initial position at startup
send_initial_position()

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
