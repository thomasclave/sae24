<?php
include("mysql.php");

// Récupération des parametres $salle et $capteur
$salle = $_POST["salle"];
$capteur = $_POST["capteur"];

// Récupération des positions des capteurs
$requete_capteurs = "
    SELECT Type, NomSalle, Pos_X, Pos_Y 
    FROM Capteur 
    WHERE NomSalle = '$salle'
    AND Type = '$capteur';";
$resultat_capteurs = mysqli_query($id_bd, $requete_capteurs);

?>