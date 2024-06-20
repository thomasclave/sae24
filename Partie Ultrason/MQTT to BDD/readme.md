# Explication du code 

## utilisation des bili

`` paho.mqtt.client`` : Bibliothèque pour la communication MQTT.
``json`` : Module pour la manipulation des données JSON.
``time`` : Module pour les fonctions liées au temps.
``  mysql.connector`` : Bibliothèque pour interagir avec une base de données MySQL.
`` datetime ``: Module pour obtenir la date et l'heure actuelles.
``collections.deque`` : Classe pour créer une liste à double extrémité sous cette forme : [x, x] 

## Variable pour stocker l'historique des zones 

``zone_history = deque(maxlen=2)``

maxlen permet de définir la taille de cette liste à max 2

## fonction qui permet déterminer la zone 

La fonction à deux paramètre qui sont capteur_id et capteur_value, puis on récupere la liste "zone_history" que c'est une vriable global que quand elle seras modiffier elle seras visible meme en dehors de cette fonction.
On dit que aucune zone à étais définis au début de cette fonction, par la suite nous testons si la valeur d'un des capteurs est à 1 alors on teste quel est le capteur qui à varier  et on dit a quel zone la personne est passé avec le capteur qui vient de changer d'état.

la condition :


    if zone is not None:
        zone_history.append(zone)

``if zone is not None :``

 - Vérifie si une zone a été définie. Si la zone est None, cela signifie qu'aucune détection valide n'a été faite et le reste du code ne s'exécute pas.

``zone_history.append(zone) :``

- Si une zone est définie, elle est ajoutée à la fin de zone_history. Si zone_history a déjà atteint sa taille maximale de 2, l'élément le plus ancien est supprimé pour faire de la place au nouvel élément.

``if len(zone_history) == 2 and zone_history[0] == zone_history[1] ``: 
- Vérifie que zone_history contient deux éléments et que les deux dernières zones sont identiques, indiquant que la personne est revenue au même capteur.

``print(f"La personne est revenue dans la zone précédente: Zone {zone - 2}")`` :
- Affiche un message indiquant que la personne est revenue dans la zone précédente.

``send_to_db(zone - 2)`` : 

- Enregistre dans la base de données la zone précédente en appelant send_to_db avec zone - 2.

``zone_history.clear() ``: 

- Vide l'historique des zones pour recommencer après la détection d'un demi-tour.


Sinon 

- la personne n'as pas fait demi tours alors on envoye la valeur de la zone avec la fonction ``send_to_db()``

Il y a aussi une condition pout voir le retour du capteur a la veleur 0 et affiche dans l'invite de commande l'ID du capteur qui est revenu à 0.

## Fonction pour Envoyer les Données à la Base de Données
