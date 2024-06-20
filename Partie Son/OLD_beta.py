#-------------------------------------------------------------------------------
# Name:        traitement_du_son.py
# Purpose:     used to create and send on MQTT server the location of a sound
#              somewhere in a room where 3 sensors are listening
#
# Author:      Marc VIGUIER
#
# Created:     02/06/2024
# Copyright:   (c) Marc VIGUIER 2024
#-------------------------------------------------------------------------------

"""
---------------------TEST V5.8 = FONCTIONNEL !!!---------------------
j'ai retiré la fonctionnalité qui écrivait un fichier JSON à la racine de ce code, à la place
le code envoi directement la donnée sur le serveur MQTT formatée comme un JSON.

ATTENTION : une partie du code est devenu obsolète. A traiter et épurer quand j'aurais le temps...

"""

import tkinter as tk
import pandas as pd
import json
import io
import sys
import paho.mqtt.client as mqtt

# la biblio JSON sert à traiter les format json
# la biblio sys donne accès à des modules et fonction utilisées par l'interpréteur, ici la sortie standard
# utilisé conjointement avec la biblio io pour écrire en string ou en binaire

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels (équivalent de 50cm en vrai)
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)
# Taille de la bordure en pixels (1 cm = 37.7953 pixels)
BORDER_SIZE = int(1 * 37.7953)

# Lire le fichier Excel et stocker les valeurs des trois feuilles dans des DataFrames séparés
excel_file = 'matrices_tournees.xlsx'  # Remplacez par le chemin de votre fichier Excel
df1 = pd.read_excel(excel_file, sheet_name='AtenuationC1', header=None)
df2 = pd.read_excel(excel_file, sheet_name='AtenuationC2', header=None)
df3 = pd.read_excel(excel_file, sheet_name='AtenuationC3', header=None)

# Convertir chaque DataFrame en une liste de listes
values1 = df1.values.tolist()
values2 = df2.values.tolist()
values3 = df3.values.tolist()

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction pour convertir un nombre décimal en binaire
def convertir_en_binaire(nombre_decimal):
    # Vérifier que le nombre est dans la plage de 0 à 4003
    if nombre_decimal < 0 or nombre_decimal > 4003:
        return "Le code à un soucis, le nombre doit être compris entre 0 et 4500."

    # Si le nombre est 0, retourner directement "0"
    if nombre_decimal == 0:
        return "0"

    # Variable pour stocker le résultat binaire
    resultat_binaire = ""

    # Boucle pour convertir le nombre décimal en binaire
    while nombre_decimal > 0:
        bit = nombre_decimal % 2  # Obtenir le bit de poids faible
        resultat_binaire = str(bit) + resultat_binaire  # Ajouter le bit à gauche du résultat
        nombre_decimal = nombre_decimal // 2  # Diviser le nombre décimal par 2
        nombre_decimal = int(nombre_decimal)

    return resultat_binaire

# Fonction pour capturer la sortie standard
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        # sert à encapsuler les données sortantes sur la sortie standard afin de les capturer dans un fichier
        with Capturing() as output:
            print(f"La case à été cliquée en ligne {row}, et colonne {col}\n")
            # Affiche les valeurs correspondantes des trois feuilles
            value1 = values1[row][col]
            value2 = values2[row][col]
            value3 = values3[row][col]
            print(f"Valeur en ligne {row}, et colonne {col} pour le : ")
            print(f"Capteur1: {value1}")
            print(f"Capteur2: {value2}")
            print(f"Capteur3: {value3}\n")
            # Simule l'effet de bouton enfoncé
            canvas.itemconfig(grid_ids[row][col], fill='darkgray')
            root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
            move_circle(row, col)

            print(f"Action sur les capteurs 1, 2 et 3 en cours...\n")
            value1 = int(value1*1000)
            nombre_decimal = value1
            binaire = convertir_en_binaire(nombre_decimal)
            print(f"Capteur 1, valeur de l'attenuation en binaire : {binaire}:01")

            value2 = int(value2*1000)
            nombre_decimal = value2
            binaire = convertir_en_binaire(nombre_decimal)
            print(f"Capteur 2, valeur de l'attenuation en binaire : {binaire}:10")

            value3 = int(value3*1000)
            nombre_decimal = value3
            binaire = convertir_en_binaire(nombre_decimal)
            print(f"Capteur 3, valeur de l'attenuation en binaire : {binaire}:11\n\n")

            #les problèmes de . entre les chiffre étaient liés au fait que le code était donné en string au niveau
            # du sous programme de convertion, et le soucis du .0 à la fin était du à un float sur la valeur rendu ici en value1, value2, etc.
            # j'ai donc transformé ces valeurs en int() et le tour à été joué :)

        sauvegarder_json(output)

def sauvegarder_json(output):
    """
    Fonction pour éditer les informations des capteurs et les envoyer sur le site, ils sont identifiés avec leurs
    numéros en binaire : 01, 10 et 11 à la fin des lignes.
    """
    capteurs = {}
    for ligne in output:
        if "Capteur" in ligne and "binaire" in ligne:

            client = mqtt.Client() # Créer une instance du client
            client.username_pw_set("CaptS1", "a") # ID et MDP de connexion
            client.connect("192.168.102.250", 1883)
            #On vient couper la ligne en tronçons à chaque ":"
            parts = ligne.split(":")
            capteur = parts[0].split(",")[0].strip()
            valeur = parts[1].strip()
            numero = parts[2].strip()
            capteurs[capteur] = valeur

            #on viens créer un topic pour chaque capteur
            topic = "sae24/E102/son/"+capteur

            #la donnée formatée le sera de la sorte : le nombre binaire du capteur devant la valeur.
            data = {
                "valeur": numero+capteurs[capteur]
            }

            #on publish le topic et on se déconnecte à la fin
            client.publish(topic, json.dumps(data))
            client.disconnect()

# Fonction pour réinitialiser la grille
def reset_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            canvas.itemconfig(grid_ids[row][col], fill='white')
    # Réinitialise la position du cercle
    move_circle(0, 0)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("16x16 Grid Interface")

# Crée un canevas pour afficher les cases et le cercle
canvas = tk.Canvas(root, width=GRID_SIZE * CASE_SIZE + 2 * BORDER_SIZE, height=GRID_SIZE * CASE_SIZE + 2 * BORDER_SIZE)
canvas.pack()

# Dessine les cases sur le canevas
grid_ids = []
for row in range(GRID_SIZE):
    row_ids = []
    for col in range(GRID_SIZE):
        x1 = col * CASE_SIZE + BORDER_SIZE
        y1 = row * CASE_SIZE + BORDER_SIZE
        x2 = x1 + CASE_SIZE
        y2 = y1 + CASE_SIZE
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
        row_ids.append(rect_id)
    grid_ids.append(row_ids)

# Dessine un cercle rouge initialement au coin supérieur gauche
circle_id = canvas.create_oval(BORDER_SIZE, BORDER_SIZE, BORDER_SIZE + CIRCLE_SIZE, BORDER_SIZE + CIRCLE_SIZE, fill='red')

# Lier l'événement de clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Crée un bouton pour réinitialiser la grille
reset_button = tk.Button(root, text="Réinitialiser la grille", command=reset_grid)
reset_button.pack()

# Lance la boucle principale de l'interface graphique
root.mainloop()