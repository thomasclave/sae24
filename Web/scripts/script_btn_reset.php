<?php
// Include the necessary dependencies (database connection, etc.)
include("../script_bdd/mysql.php");
session_start();

// Retrieve the values of room and sensor from the session
$salle = $_SESSION["salle"];
$capteur = $_SESSION["capteur"];

if ($capteur == "Son") {
    // Query to reset all positions of the person according to the selected room and sensor
    $requete_reset_son = "DELETE FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
    $resultat_reset_son = mysqli_query($id_bd, $requete_reset_son);
} elseif ($capteur == "Ultrason") {
    // Query to retrieve the last position of the person
    $requete_personne = "SELECT IDdata, X, Y, Date, Time FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur' ORDER BY Date DESC, Time DESC LIMIT 1";
    $resultat_personne = mysqli_query($id_bd, $requete_personne);

    if (mysqli_num_rows($resultat_personne) > 0) {
        $row = mysqli_fetch_assoc($resultat_personne);
        $LastID = $row['IDdata'];
        $LastX = $row['X'];
        $LastY = $row['Y'];
        $LastDate = $row['Date'];
        $LastTime = $row['Time'];

        // Query to reset all positions of the person
        $requete_reset = "DELETE FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
        $resultat_reset = mysqli_query($id_bd, $requete_reset);

        // Query to reinsert the last position of the person
        $requete_reinsert = "INSERT INTO Data (IDdata, X, Y, Date, Time, TypeCapt, NomSalle) VALUES ('$LastID', '$LastX', '$LastY', '$LastDate', '$LastTime', '$capteur', '$salle')";
        $resultat_reinsert = mysqli_query($id_bd, $requete_reinsert);
    }
}
?>
