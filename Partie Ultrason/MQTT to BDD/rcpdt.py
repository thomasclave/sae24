import paho.mqtt.client as mqtt
import json
import time
import mysql.connector
from datetime import datetime
from collections import deque

# Global variable to store the zone history
zone_history = deque(maxlen=2)

# Function to check the state of the sensors and determine the zone
def determine_zone(capteur_id, capteur_value):
    global zone_history

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
        # Add the new zone to the history
        zone_history.append(zone)

        # Check if the person has turned back
        if len(zone_history) == 2 and zone_history[0] == zone_history[1]:
            print(f"La personne est revenue dans la zone précédente: Zone {zone - 2}")
            send_to_db(zone - 2)
            zone_history.clear()  # Reset history after detecting turn back
        else:
            print(f"La personne est dans la zone {zone}")
            send_to_db(zone)
    
    if capteur_value == "0":
        print(f"{capteur_id} est revenu à 0, aucune mise à jour de la zone.")
        # The sensor has returned to 0, no zone update.

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
        """, (x, y, date_str, time_str, "Ultrason", "E102"))  # Assuming IDcapteur corresponds to x
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Données insérées : X={x}, Y={y}, Date={date_str}, Time={time_str}")
    except mysql.connector.Error as err:
        print(f"Erreur : {err}")

# Function to send initial position to the database
def send_initial_position():
    print("Envoi de la position initiale: Zone 1")
    send_to_db(1)


# Define callback functions for different MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic after connecting to the broker
    client.subscribe("sae24/+/ultra")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = str(msg.payload.decode("utf-8")) # Decode the message in UTF-8
    print(f"Message reçu sur le topic {topic} : {payload}")
    try:
        data = json.loads(payload)
        capteur_id = data['id']
        capteur_value = data['data']
        determine_zone(capteur_id, capteur_value)  # Check the zone after each data addition
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON pour le message sur le topic {topic} : {payload}")

# Create an MQTT client
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Configure the MQTT broker (address, port, and optionally credentials)
broker_address = "192.168.102.250"
broker_port = 1883
username = "CaptU1"
password = "a"

# If the broker requires a username and password
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Send the initial position at startup
send_initial_position()

# Loop to handle network messages and MQTT callbacks
client.loop_start()

try:
    # Infinite loop to keep the program running
    while True:
        time.sleep(1)  # Pause to avoid overloading the CPU

except KeyboardInterrupt:
    # Properly stop the MQTT loop in case of user interruption
    print("Interruption du programme. Fermeture de la connexion MQTT...")
    client.loop_stop()
    client.disconnect()
