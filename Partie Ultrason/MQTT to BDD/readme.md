## Explication du code 

# utilisation des bili

paho.mqtt.client : Bibliothèque pour la communication MQTT.
json : Module pour la manipulation des données JSON.
time : Module pour les fonctions liées au temps.
mysql.connector : Bibliothèque pour interagir avec une base de données MySQL.
datetime : Module pour obtenir la date et l'heure actuelles.
collections.deque : Classe pour créer une liste à double extrémité sous cette forme : [x, x] 

# Variable pour stocker l'historique des zones 

zone_history = deque(maxlen=2)

maxlen permet de définir la taille de cette liste à max 2

# fonction qui permet déterminer la zone 

cette fonction à deuc paramètre qui sont capteur_id et capteur_value, puis on récupere la liste "zone_history" que c'est une vriable global que quand elle seras modiffier elle seras visible meme en dehors de cette fonction.
On dit que aucune zone à étais définis au début de cette fonction, par la suite nous testons si la valeur d'un des capteurs est à 1 alors on teste quel est le capteur qui à varier  et on dit a quel zone le capteur vient de passer.
