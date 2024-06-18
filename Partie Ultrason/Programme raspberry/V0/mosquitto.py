import paho.mqtt.client as mqtt
import time
import random

def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code de retour: " + str(rc))

def on_publish(client, userdata, mid):
    print("Message publié avec l'ID: " + str(mid))

# Créer une instance du client
client = mqtt.Client()

# Spécifier l'ID utilisateur et le mot de passe
client.username_pw_set("CaptU1", "mosquitto")

client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Attacher les fonctions de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Se connecter au serveur MQTT
client.connect("192.168.102.200", 1883, 60)

# Démarrer la boucle réseau
client.loop_start()

# La donnée à envoyer
data = "Nouvelle donnée"

while True:
    # Publier une donnée sur un sujet spécifique
    client.publish("sae24/ultrason/capteur1", data, qos=0)

    # Attendre un court instant pour s'assurer que la donnée est publiée
    time.sleep(1)

# Arrêter la boucle réseau
client.loop_stop()