#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Marc
#
# Created:     02/06/2024
# Copyright:   (c) Marc 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Ne seront gardées que les versions de test réussies.


---------------------TEST V0.1---------------------
affichage d'une interface graphique en python, avec une grille de 16x16
quand on clique sur un des bouton, ça affiche le x et le y en nombre de case

import tkinter as tk

# Fonction pour initialiser la grille
def create_grid():
    for row in range(16):
        for col in range(16):
            # Crée un bouton pour chaque case
            button = tk.Button(root, width=5, height=2, command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col)

# Fonction appelée lorsqu'on clique sur un bouton
def on_click(row, col):
    print(f"Button clicked at row {row}, column {col}")

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("16x16 Grid Interface")

# Crée la grille de boutons
create_grid()

# Lance la boucle principale de l'interface graphique
root.mainloop()"""






"""
---------------------TEST V0.4---------------------
Affiche une grille 16x16, mais cette fois on compte plus en case mais en pixel,
ces derniers représentent les métriques de la salle (50 pixels pour 50cm).
Place un rond rouge à la place du capteur et le déplace lors du clic sur la
nouvelle case !


import tkinter as tk

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = event.x // CASE_SIZE
    row = event.y // CASE_SIZE
    print(f"Case clicked at row {row}, column {col}")
    move_circle(row, col)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("16x16 Grid Interface")

# Crée un canevas pour afficher les cases et le cercle
canvas = tk.Canvas(root, width=GRID_SIZE * CASE_SIZE, height=GRID_SIZE * CASE_SIZE)
canvas.pack()

# Dessine les cases sur le canevas
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x1 = col * CASE_SIZE
        y1 = row * CASE_SIZE
        x2 = x1 + CASE_SIZE
        y2 = y1 + CASE_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')

# Dessine un cercle rouge initialement au coin supérieur gauche
circle_id = canvas.create_oval(0, 0, CIRCLE_SIZE, CIRCLE_SIZE, fill='red')

# Lier l'événement de clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Lance la boucle principale de l'interface graphique
root.mainloop()"""







"""
---------------------TEST V1.3---------------------
ajout de la fonctionnalité d'historique avec un grisement des cases cliquées et
un déplacement du bouton rouge plus centré.

import tkinter as tk

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)
# Taille de la bordure en pixels (1 cm = 37.7953 pixels)
BORDER_SIZE = int(1 * 37.7953)

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        print(f"Case clicked at row {row}, column {col}")
        # Simule l'effet de bouton enfoncé
        canvas.itemconfig(grid_ids[row][col], fill='darkgray')
        root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
        move_circle(row, col)

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
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='darkgrey')
        row_ids.append(rect_id)
    grid_ids.append(row_ids)

# Dessine un cercle rouge initialement au coin supérieur gauche
circle_id = canvas.create_oval(BORDER_SIZE, BORDER_SIZE, BORDER_SIZE + CIRCLE_SIZE, BORDER_SIZE + CIRCLE_SIZE, fill='red')

# Lier l'événement de clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Lance la boucle principale de l'interface graphique
root.mainloop()"""









"""
---------------------TEST V1.7---------------------
Ajout d'un bouton reset pour remettre à zéro la grille.

import tkinter as tk

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)
# Taille de la bordure en pixels (1 cm = 37.7953 pixels)
BORDER_SIZE = int(1 * 37.7953)

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        print(f"Case clicked at row {row}, column {col}")
        # Simule l'effet de bouton enfoncé
        canvas.itemconfig(grid_ids[row][col], fill='darkgray')
        root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
        move_circle(row, col)

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
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='darkgrey')
        row_ids.append(rect_id)
    grid_ids.append(row_ids)

# Dessine un cercle rouge initialement au coin supérieur gauche
circle_id = canvas.create_oval(BORDER_SIZE, BORDER_SIZE, BORDER_SIZE + CIRCLE_SIZE, BORDER_SIZE + CIRCLE_SIZE, fill='red')

# Lier l'événement de clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Crée un bouton pour réinitialiser la grille
reset_button = tk.Button(root, text="Remise à zéro", command=reset_grid)
reset_button.pack()

# Lance la boucle principale de l'interface graphique
root.mainloop()
"""



"""
---------------------TEST V2.6---------------------
importer une feuille Excell et lire des données.

import tkinter as tk
import pandas as pd

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)
# Taille de la bordure en pixels (1 cm = 37.7953 pixels)
BORDER_SIZE = int(1 * 37.7953)

# Lire le fichier Excel et stocker les valeurs dans une liste de listes
excel_file = 'calcul_distances.xlsx'  # Remplacez par le chemin de votre fichier Excel
df = pd.read_excel(excel_file, header=None)
values = df.values.tolist()

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        print(f"Case clicked at row {row}, column {col}")
        # Affiche la valeur correspondante de la cellule Excel
        value = values[row][col]
        print(f"Value at row {row}, column {col}: {value}")
        # Simule l'effet de bouton enfoncé
        canvas.itemconfig(grid_ids[row][col], fill='darkgray')
        root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
        move_circle(row, col)

# Fonction pour réinitialiser la grille
def reset_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            canvas.itemconfig(grid_ids[row][col], fill='gray')
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
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill='gray', outline='black')
        row_ids.append(rect_id)
    grid_ids.append(row_ids)

# Dessine un cercle rouge initialement au coin supérieur gauche
circle_id = canvas.create_oval(BORDER_SIZE, BORDER_SIZE, BORDER_SIZE + CIRCLE_SIZE, BORDER_SIZE + CIRCLE_SIZE, fill='red')

# Lier l'événement de clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Crée un bouton pour réinitialiser la grille
reset_button = tk.Button(root, text="Reset Grid", command=reset_grid)
reset_button.pack()

# Lance la boucle principale de l'interface graphique
root.mainloop()
"""







"""

---------------------TEST V3.2 = FONCTIONNEL !!!---------------------
Ajout fontionnalité : afficher la ligne, la colonne et la valeur correspondante
à la case du tableau excell qui s'y rapporte.

ATTENTION : il faut absolument installer :

pip install openpyxl




import tkinter as tk
import pandas as pd

# Taille de la grille
GRID_SIZE = 16
# Taille d'une case en pixels (équivalent de 50cm en vrai)
CASE_SIZE = 50
# Taille du cercle (80% de la taille de la case)
CIRCLE_SIZE = int(CASE_SIZE * 0.8)
# Taille de la bordure en pixels (1 cm = 37.7953 pixels)
BORDER_SIZE = int(1 * 37.7953)

# Lire le fichier Excel et stocker les valeurs dans une liste de listes
excel_file = 'calcul_distances.xlsx'  # Remplacez par le chemin de votre fichier Excel
df = pd.read_excel(excel_file, header=None)
values = df.values.tolist()

# Fonction pour déplacer le cercle sur le canevas
def move_circle(row, col):
    x = col * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en x
    y = row * CASE_SIZE + CASE_SIZE // 2 + BORDER_SIZE  # Centre de la case en y
    offset = CIRCLE_SIZE // 2
    canvas.coords(circle_id, x - offset, y - offset, x + offset, y + offset)

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        print(f"Case clicked at row {row}, column {col}")
        # Affiche la valeur correspondante de la cellule Excel
        value = values[row][col]
        print(f"Value at row {row}, column {col}: {value}")
        # Simule l'effet de bouton enfoncé
        canvas.itemconfig(grid_ids[row][col], fill='darkgray')
        root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
        move_circle(row, col)

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
reset_button = tk.Button(root, text="Reset Grid", command=reset_grid)
reset_button.pack()

# Lance la boucle principale de l'interface graphique
root.mainloop()

"""

"""
---------------------TEST V3.6 = FONCTIONNEL !!!---------------------
#ajout de plusieurs feuille excell afin d'avoir trois valeurs des trois capteurs !!!!

"""

"""
import tkinter as tk
import pandas as pd

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

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
        print(f"La case à été cliquée en ligne {row}, et colonne {col}")
        # Affiche les valeurs correspondantes des trois feuilles
        value1 = values1[row][col]
        value2 = values2[row][col]
        value3 = values3[row][col]
        print(f"Valeur en ligne {row}, et colonne {col} pour le Capteur1: {value1}")
        print(f"Valeur en ligne {row}, et colonne {col} pour le Capteur2: {value2}")
        print(f"Valeur en ligne {row}, et colonne {col} pour le Capteur3: {value3}")
        # Simule l'effet de bouton enfoncé
        canvas.itemconfig(grid_ids[row][col], fill='darkgray')
        root.after(100, lambda: canvas.itemconfig(grid_ids[row][col], fill='gray'))
        move_circle(row, col)

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
"""







"""
---------------------TEST V4.7 = FONCTIONNEL !!!---------------------
# Ajout fonctionnalité convertion decimal / binaire + action pour les trois capteurs + dialogue invite commande

# permet de convertir en binaire MAIS multiplie par 1000 avant (pour éviter les nombre binaires infinis de chiffres à virgules)

"""
"""

import tkinter as tk
import pandas as pd

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
    # Vérifier que le nombre est dans la plage de 0 à 4500
    if nombre_decimal < 0 or nombre_decimal > 4500:
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

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
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
        """
        """ double commentaires sinon les vrais commentaires n'en sont plus...
        #   EXEMPLE de fonctionnement :
                print(f"Capteur 1 : on va prendre le nombre décimal {value1} et le multiplié par 1000 avant de le convertir en en binaire.")

                affiché : "on va prendre le nombre décimal 0.022 et le multiplié par 1000 avant de le convertir en en binaire."

                value1 = int(value1*1000)
                print(f"Le nombre décimal à virgule est devenu le nombre {value1}.")

                affiché : "Le nombre décimal à virgule est devenu le nombre 22."

                nombre_decimal = value1
                binaire = convertir_en_binaire(nombre_decimal)
                print(f"Cela correspond en binaire à {binaire}.\n\n")

                affiché : "Cela correspond en binaire à 10110."

        """
        """
        print(f"Action sur les capteurs 1, 2 et 3 en cours...\n")
        value1 = int(value1*1000)
        nombre_decimal = value1
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 1, valeur de l'attenuation en binaire : {binaire}.")

        value2 = int(value2*1000)
        nombre_decimal = value2
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 2, valeur de l'attenuation en binaire : {binaire}.")

        value3 = int(value3*1000)
        nombre_decimal = value3
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 3, valeur de l'attenuation en binaire : {binaire}.\n\n")



        #les problèmes de . entre les chiffre étaient liés au fait que le code était donné en string au niveau
        # du sous programme de convertion, et le soucis du .0 à la fin était du à un float sur la valeur rendu ici en value1, value2, etc.
        # j'ai donc transformer ces valeurs en int() et le tour à été joué :)

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
"""







"""
---------------------TEST V5.1 = FONCTIONNEL !!!---------------------
# Ajout fonctionnalité enregistrement info dans fichier JSON

"""

import tkinter as tk
import pandas as pd

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
    # Vérifier que le nombre est dans la plage de 0 à 4500
    if nombre_decimal < 0 or nombre_decimal > 4500:
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

# Fonction appelée lorsqu'on clique sur une case
def on_click(event):
    col = (event.x - BORDER_SIZE) // CASE_SIZE
    row = (event.y - BORDER_SIZE) // CASE_SIZE
    if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:  # Vérifie si le clic est dans les limites de la grille
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
        """
           EXEMPLE de fonctionnement :
                print(f"Capteur 1 : on va prendre le nombre décimal {value1} et le multiplié par 1000 avant de le convertir en en binaire.")

                affiché : "on va prendre le nombre décimal 0.022 et le multiplié par 1000 avant de le convertir en en binaire."

                value1 = int(value1*1000)
                print(f"Le nombre décimal à virgule est devenu le nombre {value1}.")

                affiché : "Le nombre décimal à virgule est devenu le nombre 22."

                nombre_decimal = value1
                binaire = convertir_en_binaire(nombre_decimal)
                print(f"Cela correspond en binaire à {binaire}.\n\n")

                affiché : "Cela correspond en binaire à 10110."

        """
        print(f"Action sur les capteurs 1, 2 et 3 en cours...\n")
        value1 = int(value1*1000)
        nombre_decimal = value1
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 1, valeur de l'attenuation en binaire : {binaire}.")

        value2 = int(value2*1000)
        nombre_decimal = value2
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 2, valeur de l'attenuation en binaire : {binaire}.")

        value3 = int(value3*1000)
        nombre_decimal = value3
        binaire = convertir_en_binaire(nombre_decimal)
        print(f"Capteur 3, valeur de l'attenuation en binaire : {binaire}.\n\n")



        #les problèmes de . entre les chiffre étaient liés au fait que le code était donné en string au niveau
        # du sous programme de convertion, et le soucis du .0 à la fin était du à un float sur la valeur rendu ici en value1, value2, etc.
        # j'ai donc transformer ces valeurs en int() et le tour à été joué :)

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