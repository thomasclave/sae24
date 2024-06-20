# Dans cette nouvelle version (v2)
*Optimiser le programme, nouveau fonctionnement, simplification des communications avec le serveur MQTT*

Remarque: Pour chaque Raspberry, nous copions ce programme et nous modifions le code pour les informations suivantes correspondes aux capteurs:
- Identifiant de connexion au serveur MQTT: CaptU1, CaptU2, CaptU3
- Le champ id du message MQTT: capteur1, capteur2, capteur3

Serveur: 192.168.102.250
Raspberry1 (capteur1): 192.168.102.247
Raspberry2 (capteur2): 192.168.102.248
Raspberry3 (capteur3): 192.168.102.249

-> le script est lancé automatiquement par le système au démarrage grâce à crontab:
crontab -e
"
@reboot sleep 10 && python3 /home/pi/Dexter/GrovePi/Software/Python/main.py
"


# Installation dependance en +
pip3 install paho-mqtt
pip3 install typing_extensions



# Utilisation
1. Allumer le serveur MQTT et le rendre disponible sur le réseau
2. Mettre un obstacle, pour faire office de seuil, et pour rendre les mesures plus stables. !! Il est maintenant possible de ne pas mettre d'obstacle !!
3. Alimenter les Raspberry (lancement automatique du programme)
Remarque: Si le serveur MQTT s’arrête en cours de route ou n'est pas disponible lors du lancement du programme, alors le programme s’arrêtera

-> Infos: Si le serveur MQTT ne fonctionne pas ou plus, alors il faut relancer les RPI


# Informations globales et objectifs du programme
- Récupérations des mesures de distances toutes les 200 millisecondes
- Filtrer les mesures pour n'avoir que les vraies mesures (pas 496, 497, 65535...)
- envoyer l'information de présence d'obstacle (0 ou 1) à un serveur MQTT uniquement en cas de changement d'état
- utilisation d'une LED pour informer si en phase d'initialisation (allumé) ou s’il y a un obstacle
--> un obstacle doit être placé avant de lancer le programme, pour fixer un seuil de détection <--
!! Si le programme n'arrive pas à se connecter au serveur MQTT alors le programme s’arrête !!

# Fonctionnement détaillé
0. Initialisation du programme, des fonctions et des dépendances
    Fonction mqtt_connect:
        Allumer la LED
        Tanter de se connecter au serveur MQTT, avec les identifiants de connexions
        Boucler tant que la connexion n'est pas initialisée (code erreur différent de 0)
        Si code d'erreur = 0 alors connecté, sortir de la boucle et éteindre la LED
    Fonction mqtt_push:
        - tester d'envoyer le message sur le serveur: le message est récupéré en paramètre
            + mettre la variable de last_mqtt_msg à valeur de message
        - si probleme (code erreur différent de 0) alors lancer la fonction mqtt_connect
    Fonction filtred_value:
        Objectif: Filtrer les erreurs de mesures
        - Prendre 3 mesures à la suite, tout en excluant la valeur 65535 (refaire la mesure dans ce cas)
        - mesures l'écart entre les 3 mesures: si elles sont à plus de 4 unités de différence alors fausse valeur, donc ne rien remonter (0)+allumer LED, sinon remonter la valeur moyenne entière+éteindre la LED. De plus, la mesure doit <500

1. Connexion au serveur MQTT
    Exécuter la fonction mqtt_connect

2. Déterminer la valeur du seuil à partir duquel sera détecté un obstacle
    - Exécuter la fonction filtred_value et si valeur < 10 alors boucler, sinon enregistrer la valeur-5 comme seuil

3. envoyer 0 sur le serveur MQTT (pas obstacle)

4. Lecture des mesures
    - récupérer la valeur de filtred_value et la stocker dans une variable
    - si la valeur et plus petite que seuil et est différent de 0 & last_mqtt_msg contient data !=1 alors nouvelle obstacle: exécuter fonction mqtt_push de la valeur 1 + Allumer la LED
        sinon si last_mqtt_msg contient data !=0: (plus d'obstacle) exécuter fonction mqtt_push de la valeur 0 + Éteindre la LED



# Résolution de problèmes
## Trop d'erreurs de mesures
Trop d'erreurs de mesures sont renvoyés, ce qui faire que la fonction de filtrage renvoie toujours 0 (affichant Distance: 0cm).
![screenshot](img/Trop_erreur.png)
### Solution
Pour parer ce problème, une nouvelle mesures est prise dès que la valeur 65535 est détectée.

## Modification des conditions de la boucle for, en cours de fonctionner
Visiblement, quand la boucle for s’exécute, elle ne regarde qu’une fois sa condition de fonctionnement. Il est donc inutile et sans effet de vouloir modifier cette condition, puisque seulement le contenu de la boucle est répété.
![screenshot](img/PB_boucle-for1.png)
![screenshot](img/PB_boucle-for2.png)

### Solution
Utilisation d'une boucle while, qui elle relie sa condition de fonctionnement

-> en résolvant l'erreur du 65535, j'ai vu qu’il était possible de se soulager de la contrainte de devoir toujours mettre un obstacle de référence (servant de seuil) au démarrage du programme. Pour cela il suffi juste d’accepter les valeurs comprises entre 490 et 500 (qui correspond à la mesure max), en passant le seuil de 490 à 500.
Ainsi, la mesure max est comprise comme étant une valeur de seuil utilisable.



# Amélioration possible du programme
- Gestion des erreurs avec le serveur MQTT: Faire que le programme boucle et re essaye, au lieu de s’arrêter directement, obligeant à relancer le programme (donc les RPI)
- Que l'on puisse adapter plus facilement le programme pour un capteur en particulier (Identifiant de connexion au serveur MQTT + ID du capteur dans les messages MQTT)