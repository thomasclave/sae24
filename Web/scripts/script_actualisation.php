<?php
// Inclure les dépendances nécessaires (connexion à la base de données, etc.)
include("../script_bdd/mysql.php");
session_start();

$salle = $_SESSION["salle"];
$capteur = $_SESSION["capteur"];

// Requête pour récupérer la dernière position de la personne
$requete_personne = "SELECT X, Y FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur' ORDER BY Date DESC, Time DESC LIMIT 1";
$resultat_personne = mysqli_query($id_bd, $requete_personne);

// Vérifier s'il y a des résultats
if ($resultat_personne && mysqli_num_rows($resultat_personne) > 0) {
    // Récupérer les données de la dernière position
    $row = mysqli_fetch_assoc($resultat_personne);
    $position = array('X' => $row['X'], 'Y' => $row['Y']);
    echo json_encode($position);
} else {
    // Si aucune position n'est trouvée, retourner un objet vide
    echo json_encode(array());
}

// Fermer la connexion à la base de données
mysqli_close($id_bd);
?>
