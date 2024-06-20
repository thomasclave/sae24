import paho.mqtt.client as mqtt
import json
import time
import mysql.connector
from datetime import datetime
from collections import deque

# Variable globale pour stocker les dernières valeurs des capteurs
# Global variable to store the last values of the sensors
sensor_history = {
    "capteur1": deque(maxlen=2),
    "capteur2": deque(maxlen=2),
    "capteur3": deque(maxlen=2)
}

# Fonction pour vérifier l'état des capteurs et déterminer la zone
# Function to check the state of the sensors and determine the zone
def determine_zone(capteur_id, capteur_value):
    # Ajouter la nouvelle valeur à l'historique du capteur
    # Add the new value to the sensor's history
    sensor_history[capteur_id].append(capteur_value)

    # Vérifier si la personne est revenue en arrière
    # Check if the person has returned to the same sensor
    if len(sensor_history[capteur_id]) == 2:
        last_value = sensor_history[capteur_id][0]
        current_value = sensor_history[capteur_id][1]
        if last_value == current_value:
            print(f"La personne est revenue en arrière au capteur {capteur_id}")

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
username = "Capt1"
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
