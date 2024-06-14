#!/opt/lampp/bin/php


<?php
$idBd = mysqli_connect("localhost", "root", "passroot", "sae23")
    or die("Echec de la connexion à la base de données"); // Connect to the database or display an error message if the connection fails // Connexion à la base de données ou affichage d'un message d'erreur en cas d'échec

while (true) { // Infinite loop to continuously fetch and process data // Boucle infinie pour récupérer et traiter les données en continu
    $mqtt_broker = "mqtt.iut-blagnac.fr"; // MQTT broker URL // URL du broker MQTT
    $mqtt_topic = "AM107/by-room/+/data"; // MQTT topic to subscribe to // Sujet MQTT à s'abonner

    // Execute the MQTT subscription command and capture the JSON output // Exécuter la commande d'abonnement MQTT et capturer la sortie JSON
    $rcpjson = shell_exec('mosquitto_sub -h '.$mqtt_broker.'-t '.$mqtt_topic.' -C 1');

    // Decode the JSON data into an associative array // Décoder les données JSON en un tableau associatif
    $jsondec = json_decode($rcpjson, true);

}
?>