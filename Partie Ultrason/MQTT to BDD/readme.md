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
On dit que aucune zone à étais définis au début de cette fonction, par la suite nous testons si la valeur d'un des capteurs est à 1 alors on teste quel est le capteur qui à varier  et on dit a quel zone la personne est passé avec le capteur qui vient de changer d'état.

la condition :

if zone is not None:
        # Ajouter la nouvelle zone à l'historique
        zone_history.append(zone)

if zone is not None :
 - Vérifie si une zone a été définie. Si la zone est None, cela signifie qu'aucune détection valide n'a été faite et le reste du code ne s'exécute pas.

zone_history.append(zone) :
- Si une zone est définie, elle est ajoutée à la fin de zone_history. Si zone_history a déjà atteint sa taille maximale de 2, l'élément le plus ancien est supprimé pour faire de la place au nouvel élément.

