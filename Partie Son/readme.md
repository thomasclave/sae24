<<<<<<< HEAD:Partie Son/readme.md
AVANT TOUTES CHOSES : SI VOUS DECIDEZ DE CHANGER LE CONTENU DE L'UN DES FICHIERS 
PRESENTS, VEUILLEZ SVP UTILISER UN NOUVEAU NOM DE FICHIER COMPOSE COMME CECI :
- VOTRE PRENOM 
- LA DATTE DE MODIFICATION 
- SUIVI DU NOM DU FICHIER ORIGINEL

ex : le fichier texte1.txt > texte1.marc.02_06.txt



Ici sont les fichiers fait pour plusieurs étapes de la partie "son" du projet SAE24 :

- Le fichier excel servira à :
	Feuille 1 = tableau de données calculées (en Feuille 2) afin d'être 
	extraites et utilisées par le programme python.

	Feuille 2 = le traitement des donnée nécessaire à l'établissement :
		- des distances de chacunes des cases vis à vis de la première (haut - gauche)
		- les calculs de l'amplitude du signal et de son atténuation
		
- Un script python qui servira à :
	- Créer une interface graphique composée d'une grille de 16x16 de côté et d'un
	point représentant le premier capteur.
	- Simuler l'arrivé d'une donnée d'emplacement (cliquer sur une case choisie)
	- Déplacer le point rouge afin de garder la case choisie en mémoire
	- Possibilité de re-déplacer le point, gardant en grisé les derniers points
	- Bouton reset afin de remettre la simulation à zéro.
	- Récupération et mise en mémoire des données du fichier excel (premier capteur)
	- Renvoi dans la console des emplacement x, y du nouveau point
	- Renvoi de la donnée faite précédement dans l'extract du Excel pour la case choisie

CE QUI DOIT ENCORE ÊTRE FAIT :

- mise en place d'un fichier de log grâce à une redirection des information affichées dans la console.
- horodatage et formatage automatique du fichier de log.
=======
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
>>>>>>> origin/Branche-MARC:Partie Son/Fichiers grille, distances et simulations/LISEZ-MOI.txt
