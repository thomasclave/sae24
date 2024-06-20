Ici sont les fichiers fait pour plusieurs étapes de la partie "son" du projet SAE24 :

- Le fichier excel servira à :
	- Calcul de l'aténuation de TOUTES les cases par rapport à une case spécifique (la case détécteur en 0)
	
- Un script python qui servira à :
	- Créer une interface graphique composée d'une grille de 16x16 de côté et d'un
	point représentant le premier capteur.
	- Simuler l'arrivé d'une donnée d'emplacement (cliquer sur une case choisie)
	- Déplacer le point rouge afin de garder la case choisie en mémoire
	- Possibilité de re-déplacer le point, gardant en grisé les derniers points
	- Bouton reset afin de remettre la simulation à zéro.
	- Récupération et mise en mémoire des données du fichier excel, pour les trois capteurs
	- Renvoi dans la console des emplacement x, y des nouveaux points
	- Renvoi de la donnée faite précédement dans l'extract du Excel pour la case choisie
	- Donnée aténuation arrondi au millième
	- Encodage des données en binaire
	- Envoi MQTT au format JSON avec trois topics


fonctionne avec :

-------- python 3.10.11

-------- pip 23.3.2

avec les libraires :

-------- tkinter

-------- pandas 

-------- json

-------- io

-------- sys

-------- paho.mqtt.client

il faut installer :

-------- pip install openpyxl



Ancienne versions :

---------------------TEST V0.1---------------------

affichage d'une interface graphique en python, avec une grille de 16x16
quand on clique sur un des bouton, ça affiche le x et le y en nombre de case

---------------------TEST V0.4---------------------

Affiche une grille 16x16, mais cette fois on compte plus en case mais en pixel,
ces derniers représentent les métriques de la salle (50 pixels pour 50cm).
Place un rond rouge à la place du capteur et le déplace lors du clic sur la
nouvelle case !

---------------------TEST V1.3---------------------

ajout de la fonctionnalité d'historique avec un grisement des cases cliquées et
un déplacement du bouton rouge plus centré.

---------------------TEST V1.7---------------------

Ajout d'un bouton reset pour remettre à zéro la grille.

---------------------TEST V2.6---------------------

importer une feuille Excell et lire des données.

---------------------TEST V3.2---------------------

Ajout fontionnalité : afficher la ligne, la colonne et la valeur correspondante
à la case du tableau excell qui s'y rapporte.

ATTENTION : il faut absolument installer :

pip install openpyxl

---------------------TEST V3.6---------------------

#ajout de plusieurs feuille excell afin d'avoir trois valeurs des trois capteurs !!!!

---------------------TEST V4.7---------------------

# Ajout fonctionnalité convertion decimal / binaire + action pour les trois capteurs + dialogue invite commande

# permet de convertir en binaire MAIS multiplie par 1000 avant (pour éviter les nombre binaires infinis de chiffres à virgules)

---------------------TEST V5.5---------------------

# Ajout fonctionnalité pour capturer la sortie standard, un formatage pourresembler à un fichier lambda
JSON et donc pour enregistrer ces données dans un fichier JSON

---------------------TEST V5.8---------------------

j'ai retiré la fonctionnalité qui écrivait un fichier JSON à la racine de ce code, à la place
le code envoi directement la donnée sur le serveur MQTT formatée comme un JSON.

ATTENTION : une partie du code est devenu obsolète. A traiter et épurer quand j'aurais le temps...

