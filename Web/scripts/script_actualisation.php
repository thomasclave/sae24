<?php
// Include necessary dependencies (database connection, etc.)
include("../script_bdd/mysql.php");
session_start();

$salle = $_SESSION["salle"];
$capteur = $_SESSION["capteur"];

// Query to retrieve the latest position of the person
$requete_personne = "SELECT X, Y FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur' ORDER BY Date DESC, Time DESC LIMIT 1";
$resultat_personne = mysqli_query($id_bd, $requete_personne);

// Check if there are any results
if ($resultat_personne && mysqli_num_rows($resultat_personne) > 0) {
    // Retrieve the data of the latest position
    $row = mysqli_fetch_assoc($resultat_personne);
    $position = array('X' => $row['X'], 'Y' => $row['Y']);
    echo json_encode($position);
} else {
    // If no position is found, return an empty object
    echo json_encode(array());
}

// Close the database connection
mysqli_close($id_bd);
?>
