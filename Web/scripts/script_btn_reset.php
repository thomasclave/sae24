<?php
// Inclure les dépendances nécessaires (connexion à la base de données, etc.)
include("../script_bdd/mysql.php");
session_start();

// Récupérer les valeurs de salle et capteur depuis la session
$salle = $_SESSION["salle"];
$capteur = $_SESSION["capteur"];

// Requête pour réinitialiser toutes les positions de la personne selon la salle et le capteur sélectionnés
$requete_reset = "DELETE FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
$resultat_reset = mysqli_query($id_bd, $requete_reset);

if ($resultat_reset) {
    echo "Réinitialisation des positions réussie.";
} else {
    echo "Erreur lors de la réinitialisation des positions : " . mysqli_error($id_bd);
}

mysqli_close($id_bd);
?>
