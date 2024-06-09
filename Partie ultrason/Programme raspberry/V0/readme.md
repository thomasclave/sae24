Programme sur RPI (envoie des informations sur le serveur MQTT)

## Aspects matériel
Configuration matériel : 3 capteurs ultrason avec une LED rattachée à chacun pour indiquer la détection d’un obstacle.


## Fonctionnement du programme
0. Initialisation du capteur: Enregistrement du seuil de detection
    Indiquer que nous sommes en phase d'initialisation -> allumer la LED
    Lire la valeur reçue par le capteur et la stocker dans une variable (en gérrent les fausses mesures)
        recuperer durant une demi seconde les valeurs retournées par le capteur, regarder les écrats entre la plus petite valeur et la plus grande enregistré, different de 65535, si l'écart est acceptable (donc pas de fausse erreur) alors prendre la plus petite mesure, la baisser de 3% et l'enregistrer dans une variable (valeur de référence / seuil de détection d'obstacle), puis sortie de la phase d'initialisation (atteindre la LED)
        Sinon, relancer le teste + faire clignoter la LED 1seconde

Faire en boucle:
    1. récupérer les mesures du capteurs ultrason (toutes les 1/2 secondes)
    2. déterminer si obstacle ou non
        Si la mesure de la distance et plus faible que les valeurs de bases enregistrés au lancement    du programme.

            0 Si pas d’obstacle
            1 Si un obstacle est détecté

    3. envoyer les mesures au serveurs (si changement d’état)
        formatage de l'information: ID_capteur, valeur


source connexion mqtt: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
                       http://www.steves-internet-guide.com/publishing-messages-mqtt-client/