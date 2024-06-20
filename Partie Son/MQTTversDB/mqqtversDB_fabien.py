#-------------------------------------------------------------------------------
# Name:       mqttversDB
# Purpose:
#
# Author:      Fabien Moine
#
# Created:     18/06/2024
# Copyright:   (c) Fabien Moine 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#library to get extract the table from excel
import pandas as pd
#library to manage mqtt
import paho.mqtt.client as mqtt
#library to read and extrac data from  json
import json
#library to manage sql and push the data on the DB
import mysql.connector
#Library to get the time and the date
from datetime import datetime

a="true"
while a=="true":



    # Connecting to the sql database
    conn = mysql.connector.connect(
        host='192.168.102.250',       # host address
        user='g31',   # sql user
        password='passg31', # user's password
        database='sae24'  # database name
    )

    cursor = conn.cursor()

    #reading excel file and extracting the table that hold the attenuation value
    excel_file = 'matrices_tournees.xlsx'  #file path
    df1 = pd.read_excel(excel_file, sheet_name='AtenuationC1', header=None)
    df2 = pd.read_excel(excel_file, sheet_name='AtenuationC2', header=None)
    df3 = pd.read_excel(excel_file, sheet_name='AtenuationC3', header=None)

    #convert each dataframe to a list of list
    values1 = df1.values.tolist()
    values2 = df2.values.tolist()
    values3 = df3.values.tolist()

    #function that get each coordinates of a value in the table
    def find_positions(matrix, value_to_find):
        positions = []
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == value_to_find:
                    positions.append((x+1, y+1))
        return positions


    #function to get the shared value of different table
    def trilateration(positions1, positions2, positions3):
        # Convert position lists to sets for more efficient searching
        set1 = set(positions1)
        set2 = set(positions2)
        set3 = set(positions3)

        # Find the intersection of the three sets
        common_positions = set1.intersection(set2).intersection(set3)

        # Convert resulting set to list
        return list(common_positions)


    # list to store the mqtt messages
    messages = []

    # Function called when a connection to the broker is established
    def on_connect(client, userdata, flags, rc):
        print("Connecté avec le code de résultat " + str(rc))
        # Subscribe to the "test/topic" topic
        client.subscribe("sae24/E102/son/#")

    # Function called when a message is received
    def on_message(client, userdata, msg):
        global messages
        print("Message reçu sur le topic " + msg.topic + ": " + str(msg.payload))
        try:
            # Parse JSON message
            message_dict = json.loads(msg.payload.decode())
            #Add message to the message list
            mqtt_value = message_dict.get("valeur")
            messages.append(mqtt_value)

        except json.JSONDecodeError:
            print("Erreur de décodage du JSON")

        # Stop MQTT client after receiving 3 messages
        if len(messages) >= 3:
            client.disconnect()

    # Create a new MQTT client instance
    client = mqtt.Client()
    client.username_pw_set("CaptS2", password="a")


    client.on_connect = on_connect
    client.on_message = on_message

    #Connection to the MQTT broker
    client.connect("192.168.102.250", 1883, 60)

    #Start network loop to process MQTT events
    client.loop_forever()


    print(messages)

    """
    for loop that determine the number of the sensor based of the first 2 bits of the message
    01 for sensor1, 10 for sensor2 , 11  for sensor3
    """
    for x in range(len(messages)):
        if messages[x][:2]=="01":
            print("capteur1")
            #storing the message without the first two bits
            binaire1 = messages[x][2:]
            #translate the value into decimal
            decimal_number1 = int(binaire1, 2)
            #divide it by  1000
            amplitude1 = decimal_number1/1000
            print(amplitude1)
            #get all the possible positions for this value of attenuation
            positions1 = find_positions(values1, amplitude1)
            print(positions1)

        elif messages[x][:2]=="10":
            print("capteur2")
            binaire2 = messages[x][2:]
            decimal_number2 = int(binaire2, 2)
            amplitude2 = decimal_number2/1000
            print(amplitude2)
            positions2 = find_positions(values2, amplitude2)
            print(positions2)

        elif messages[x][:2]=="11":
            print("capteur3")

            binaire3 = messages[x][2:]
            decimal_number3 = int(binaire3, 2)
            amplitude3 = decimal_number3/1000
            print(amplitude3)
            positions3 = find_positions(values3, amplitude3)
            print(positions3)
        else:
            print ("erreur la valeur ne correspond a aucun capteur")

    #getting the position of the object by trilateration
    pos=trilateration(positions1,positions2,positions3)
    print(pos)

    #getting the current date and time to send the data in the DB
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")

    #Display the current date and time
    print("Date actuelle formatée:", formatted_date)
    print("Heure actuelle formatée:", formatted_time)

    #preparing sql query
    query = "INSERT INTO Data (X, Y, Date, Time, TypeCapt, NomSalle) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (pos[0][1], pos[0][0], formatted_date, formatted_time, "son", "E102")

    try:
        # execute the query
        cursor.execute(query, values)

        # commit change
        conn.commit()
        print("Données insérées avec succès")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
        # cancel change if there is a problem
        conn.rollback()
    finally:
        # close connexion
        cursor.close()
        conn.close()
