#-------------------------------------------------------------------------------
# Name:        rotation
# Purpose:
#
# Author:      Fabien
#
# Created:     07/06/2024
# Copyright:   (c) etud 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def rotation_matrice_90_horaire(matrice):
    n=len(matrice)
    #creation d'une d'une liste de n element initialise a 0,
    # par exemple si n = 4 ----> [0,0,0,0]
    #on combine ca avec un for in range pour cree une matrice de 0
    rotated_matrice = [[0] * n for _ in range(n)]
    #formule pour effectuer une rotation de 90 degree en sens horaire
    for i in range(n):
        for j in range(n):
            rotated_matrice[n-1-j][i] = matrice[i][j]
    return rotated_matrice

def rotation_matrice_90_antihoraire(matrice):
    n=len(matrice)
    rotated_matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrice[j][n-1-i] = matrice[i][j]
    return rotated_matrice


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    ]

B = rotation_matrice_90_horaire(A)

C= rotation_matrice_90_antihoraire(A)

print(C)
print(B)

