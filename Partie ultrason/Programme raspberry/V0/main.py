import time
import grovepi
from grovepi import *

## Variables ##
led = 3 # Connexion de la LED sur la pin D3
pinMode(led,"OUTPUT") # parametrer la LED comme sortie
digitalWrite(led,0) # Eteindre la LED
grovepi.set_bus("RPI_1") # parametrer le bus I2C pour utiliser le materiel
ultrasonic = 2 # Connexion du capteur ultrason sur la pin D4
seuil = 0


## 0 - Initialisation du capteur: Enregistrement du seuil de detection ##
init = True
digitalWrite(led,1) # Allumer la LED
while init: # Tant que le bloque initialisation n'est pas validé
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    if distance != "65535":
        print(distance)
        seuil = distance-40
        init = False
    time.sleep(0.1) # ne pas surcharger le bus I2C
digitalWrite(led,0) # Eteindre la LED




last_val = 0
while True:
    distance = grovepi.ultrasonicRead(ultrasonic) # récuperer la distance mesurée
    if distance < seuil and (distance < last_val-15 or distance > last_val+15):
        print(distance)
        last_val = distance # enregistrer le nouveau seuil
        digitalWrite(led,1) # Allumer la LED
        time.sleep(0.25)
        digitalWrite(led,0) # Eteindre la LED


    time.sleep(0.1) # ne pas surcharger le bus I2C