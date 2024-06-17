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

il faut absolument installer :

pip install openpyxl

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
