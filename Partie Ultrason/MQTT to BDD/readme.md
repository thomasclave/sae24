# Explication du code 

## utilisation des bili

`` paho.mqtt.client`` : Bibliothèque pour la communication MQTT.


``json`` : Module pour la manipulation des données JSON.


``time`` : Module pour les fonctions liées au temps.


``mysql.connector`` : Bibliothèque pour interagir avec une base de données MySQL.


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

``send_to_db()`` Nous permet de pouvoir envoyer la valeur de X a la base de donnée. Tout d'abort on définis la position y à 1 car on de bouge pas sur l'axe y.

## Fonction pour Envoyer la Position Initiale

    def send_initial_position():
        print("Envoi de la position initiale: Zone 1")
        send_to_db(1)

Cette fonction permet de définir la position initiale de la zone ou la personne se trouve logiquement. Puis l'affiche dans l'invite de commande le set de la position. En fin on envoie la position sur la base de donnée.

## Fonctions de Rappel pour les Événements MQTT

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("sae24/+/ultra")

    def on_message(client, userdata, msg):
        topic = msg.topic
        payload = str(msg.payload.decode("utf-8"))
        print(f"Message reçu sur le topic {topic} : {payload}")
        try:
            data = json.loads(payload)
            capteur_id = data['id']
            capteur_value = data['data']
            determine_zone(capteur_id, capteur_value)
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON pour le message sur le topic {topic} : {payload}")

### Fonction on_connect

La fonction ``on_connect`` est déclenchée lorsque le client MQTT se connecte avec succès au broker MQTT. Elle prend les paramètres suivants :

client : L'instance du client MQTT.


userdata : Les données définies par l'utilisateur, non utilisées dans ce contexte.


flags : Les drapeaux de connexion, non utilisés ici.


rc : Le code de résultat de la connexion, où 0 signifie une connexion réussie.


Lorsqu'une connexion est établie avec succès, la fonction :

- Affiche un message confirmant la connexion réussie avec le code de résultat.
- Abonne le client à sae24/+/ultra pour qu'il puisse recevoir les messages publiés sur ce topics.


### Fonction on_message

La fonction ``on_message`` est déclenchée chaque fois qu'un message est reçu sur un topic auquel le client est abonné. Elle prend les paramètres suivants :

client : L'instance du client MQTT.


userdata : Les données définies par l'utilisateur, non utilisées dans ce contexte.


msg : Le message reçu, contenant le topic et le contenu (``payload``).


Lorsqu'un message est reçu, la fonction :

- Extrait le topic du message et le contenu (``payload``), puis décode le payload en UTF-8 pour le rendre lisible.
- Affiche le topic et le payload du message reçu.
- Tente de convertir le payload en objet JSON. 

Si la conversion réussit :


- Extrait l'ID du capteur (``capteur_id``) et la valeur du capteur (``capteur_value``) des données JSON.
- Appelle la fonction ``determine_zone`` avec ``capteur_id `` et ``capteur_value`` pour vérifier et mettre à jour la zone.
- Si le payload ne peut pas être décodé en JSON, affiche un message d'erreur indiquant que le décodage JSON a échoué.


En résumé, ces fonctions gèrent la connexion au broker MQTT et le traitement des messages reçus, en s'abonnant aux topics pertinents et en manipulant les données des capteurs pour déterminer les zones et détecter les retours en arrière.

### Configuration et Connexion du Client MQTT

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    broker_address = "192.168.102.250"
    broker_port = 1883
    username = "CaptU1"
    password = "a"

    client.username_pw_set(username, password)
    client.connect(broker_address, broker_port, 60)

Ce segment de code crée et configure un client MQTT pour se connecter à un broker MQTT, s'abonner à des topics, et traiter les messages reçus.

1. **Création d'une instance de client MQTT** :

   ```python
   client = mqtt.Client()
   ```

   - Cette ligne crée une nouvelle instance de client MQTT en utilisant la bibliothèque Paho MQTT. Cette instance sera utilisée pour se connecter au broker MQTT, s'abonner à des topics, publier et recevoir des messages.

2. **Assignation des fonctions de rappel** :

   ```python
   client.on_connect = on_connect
   client.on_message = on_message
   ```

   - `client.on_connect = on_connect` : Cette ligne assigne la fonction `on_connect` comme fonction de rappel (callback) pour les événements de connexion. Cela signifie que la fonction `on_connect` sera appelée chaque fois que le client se connecte au broker MQTT.
   - `client.on_message = on_message` : Cette ligne assigne la fonction `on_message` comme fonction de rappel pour les événements de réception de messages. La fonction `on_message` sera appelée chaque fois que le client reçoit un message sur un topic
    auquel il est abonné.

3. **Configuration de l'adresse du broker MQTT** :

   ```python
   broker_address = "192.168.102.250"
   broker_port = 1883
   username = "CaptU1"
   password = "a"
   ```

   - `broker_address` : Cette variable stocke l'adresse IP du broker MQTT. Dans ce cas, le broker se trouve à l'adresse `192.168.102.250`.
   - `broker_port` : Cette variable stocke le numéro de port sur lequel le broker MQTT écoute les connexions entrantes. Le port standard pour MQTT est `1883`.
   - `username` : Cette variable stocke le nom d'utilisateur utilisé pour s'authentifier auprès du broker MQTT.
   - `password` : Cette variable stocke le mot de passe associé au nom d'utilisateur pour s'authentifier auprès du broker MQTT.

4. **Configuration des identifiants d'authentification** :

   ```python
   client.username_pw_set(username, password)
   ```

   - Cette ligne configure les identifiants d'authentification pour le client MQTT en utilisant les variables `username` et `password`. Cela permet au client de s'authentifier auprès du broker MQTT lors de la connexion.

5. **Connexion au broker MQTT** :

   ```python
   client.connect(broker_address, broker_port, 60)
   ```

   - `client.connect(broker_address, broker_port, 60)` : Cette ligne initie une connexion au broker MQTT en utilisant l'adresse et le port spécifiés. Le dernier argument (`60`) est le délai d'attente (keepalive) en secondes. Il définit la fréquence à laquelle le client doit envoyer des messages de maintien de connexion au broker pour indiquer qu'il est toujours actif.

En résumé, ce segment de code crée un client MQTT, configure les fonctions de rappel pour les événements de connexion et de réception de messages, définit les paramètres de connexion au broker MQTT, configure l'authentification et initie la connexion au broker MQTT. Cela permet au client de se connecter au broker, de s'abonner à des topics et de recevoir des messages.

## Envoi de la Position Initiale, Démarrage de la Boucle MQTT et Gestion des Interruptions

Ce segment de code envoie la position initiale à la base de données, démarre la boucle de traitement des messages MQTT, et gère les interruptions du programme.

```python
send_initial_position()

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interruption du programme. Fermeture de la connexion MQTT...")
    client.loop_stop()
    client.disconnect()
```

1. **Envoi de la Position Initiale** :

   ```python
   send_initial_position()
   ```

   - **send_initial_position()** : Cette ligne appelle la fonction `send_initial_position` qui envoie la position initiale (Zone 1) à la base de données. Cette fonction est exécutée une fois au démarrage du programme pour enregistrer la position de départ.

2. **Démarrage de la Boucle de Traitement des Messages MQTT** :

   ```python
   client.loop_start()
   ```

   - **client.loop_start()** : Cette ligne démarre une boucle en arrière-plan qui permet au client MQTT de traiter les messages et d'appeler les fonctions de rappel (`on_connect` et `on_message`) lorsque des événements MQTT se produisent. Cela permet au client de rester connecté au broker et de recevoir des messages en continu.

3. **Boucle Infinie pour Maintenir le Programme en Exécution** :

   ```python
   try:
       while True:
           time.sleep(1)
   ```

   - **try** : Le bloc `try` commence ici et inclut une boucle infinie pour maintenir le programme en cours d'exécution.
   - **while True** : Cette ligne crée une boucle infinie, ce qui signifie que le code à l'intérieur de la boucle s'exécutera en continu jusqu'à ce que la boucle soit interrompue.
   - **time.sleep(1)** : Cette ligne met le programme en pause pendant 1 seconde à chaque itération de la boucle. Cela permet d'éviter une surcharge du processeur en introduisant une courte pause entre les cycles de la boucle.

4. **Gestion des Interruptions par l'Utilisateur** :

   ```python
   except KeyboardInterrupt:
       print("Interruption du programme. Fermeture de la connexion MQTT...")
       client.loop_stop()
       client.disconnect()
   ```

   - **except KeyboardInterrupt** : Ce bloc intercepte les interruptions du clavier (par exemple, lorsque l'utilisateur appuie sur `Ctrl+C`).
   - **print("Interruption du programme. Fermeture de la connexion MQTT...")** : Affiche un message indiquant que le programme est interrompu et que la connexion MQTT va être fermée.
   - **client.loop_stop()** : Arrête la boucle MQTT proprement. Cela signifie que le client MQTT cesse de traiter les messages et les événements en arrière-plan.
   - **client.disconnect()** : Déconnecte le client du broker MQTT. Cela ferme la connexion de manière appropriée et assure que toutes les ressources sont libérées correctement.

### En Résumé

- **send_initial_position()** : Envoie la position initiale à la base de données pour enregistrer la position de départ.
- **client.loop_start()** : Démarre une boucle en arrière-plan pour permettre au client MQTT de traiter les messages et les événements en continu.
- **Boucle infinie** : Maintient le programme en cours d'exécution avec une pause de 1 seconde entre chaque cycle pour éviter de surcharger le processeur.
- **Gestion des interruptions** : Intercepte les interruptions de clavier, arrête proprement la boucle MQTT et déconnecte le client du broker MQTT, garantissant ainsi une fermeture propre et sécurisée du programme.