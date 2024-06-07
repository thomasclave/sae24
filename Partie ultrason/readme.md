Programme sur RPI (envoie des informations sur le serveur MQTT)

## Aspects matériel
Configuration matériel : 3 capteurs ultrason avec une LED rattachée à chacun pour indiquer la détection d’un obstacle.




## Fonctionnement du programme
0. Initialisation : Lancement du programme : déterminer les distances par défaut (sans obstacle)

1. récupérer les mesures des capteurs ultrason (tous les 1/2 secondes)
2. déterminer si obstacle ou non
    Si la mesure de la distance et plus faible que les valeurs de bases enregistrés au lancement    du programme.

        0 Si pas d’obstacle
        1 Si un obstacle est détecté

3. envoyer les mesures au serveurs (si changement d’état)


            Traduction de l’information :
            ID_capteur, valeur