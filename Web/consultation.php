<?php
include("./script_bdd/mysql.php");
session_start();

// Vérification si des données ont été postées depuis le formulaire
if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
    $salle = $_POST["salle"];
    $capteur = $_POST["capteur"];

    $_SESSION["salle"] = $salle;
    $_SESSION["capteur"] = $capteur;

    // Requête pour récupérer les dimensions de la salle sélectionnée
    $requete_dimensions = "SELECT Longueur, Largeur FROM Salle WHERE NomSalle = '$salle'";
    $resultat_dimensions = mysqli_query($id_bd, $requete_dimensions);
    $row_dimensions = mysqli_fetch_assoc($resultat_dimensions);
    $longueur = $row_dimensions['Longueur'];
    $largeur = $row_dimensions['Largeur'];

    // Requête pour récupérer les positions des capteurs
    $requete_capteurs = "SELECT Pos_X, Pos_Y FROM Capteur WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
    $resultat_capteurs = mysqli_query($id_bd, $requete_capteurs);

    // Requête pour récupérer la dernière position de la personne
    $requete_personne = "SELECT X, Y FROM Data WHERE NomSalle = '$salle' AND TypeCapt = '$capteur' ORDER BY Date DESC, Time DESC LIMIT 1";
    $resultat_personne = mysqli_query($id_bd, $requete_personne);
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation</title>

    <!-- Liens CSS -->
    <link rel="stylesheet" href="./css/style.css">

    <!-- Liens vers les polices -->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
</head>

<body>
    <!-- Barre de navigation -->
    <nav class="navbar">
        <a class="nav-nom" href="./index.php">SAE24</a>
        <ul class="nav-links">
            <li><a href="./index.php">Accueil</a></li>
            <li class="active"><a href="./consultation.php">Consultation</a></li>
            <li><a href="./mentions-legales.html">Mentions Légales</a></li>
        </ul>
    </nav>

    <!-- Titre -->
    <header>
        <h2>Consultation</h2>
    </header>

    <main>
        <form action="consultation.php" method="POST">
            <label for="salle">Sélectionnez une salle :</label>
            <select name="salle" id="salle" required>
                <option value="">Choisissez une salle</option>
                <?php
                // Affichage des options de sélection des salles
                $requete_salles = "SELECT NomSalle FROM Salle";
                $resultat_salles = mysqli_query($id_bd, $requete_salles);
                while ($row = mysqli_fetch_assoc($resultat_salles)) {
                    $nomSalle = $row['NomSalle'];
                    $selected = (isset($salle) && $nomSalle == $salle) ? "selected" : "";
                    echo "<option value='$nomSalle' $selected>$nomSalle</option>";
                }
                ?>
            </select>
            <br><br>

            <label for="capteur">Sélectionnez un type de capteur :</label>
            <select name="capteur" id="capteur" required>
                <option value="Son" <?php echo (isset($capteur) && $capteur == "Son") ? "selected" : ""; ?>>Son</option>
                <option value="Ultrason" <?php echo (isset($capteur) && $capteur == "Ultrason") ? "selected" : ""; ?>>Ultrason</option>
            </select>
            <br><br>

            <input type="submit" value="Consulter">
        </form>

        <br><br>

        <?php
        if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
            if ($resultat_dimensions && mysqli_num_rows($resultat_dimensions) > 0) {
                echo "<h2>Positions $capteur dans la salle $salle :</h2>";
                
                if ($capteur == 'Son') {
                    
                    // Bouton de réinitialisation
                    echo "<button id='reset-button' class='reset-button'>Réinitialiser le parcours</button>";
                    echo "<br>";
                    echo "<table class='salle-table'>";
                    for ($y = 1; $y <= $largeur; $y++) {
                        echo "<tr>";
                        for ($x = 1; $x <= $longueur; $x++) {
                            $case_class = "case_vide";
                            // Vérification si la position correspond à un capteur
                            mysqli_data_seek($resultat_capteurs, 0); // Réinitialise l'itérateur
                            while ($capteur_row = mysqli_fetch_assoc($resultat_capteurs)) {
                                if ($capteur_row['Pos_X'] == $x && $capteur_row['Pos_Y'] == $y) {
                                    $case_class = "case_rouge"; // Classe pour les capteurs
                                    break;
                                }
                            }

                            // Vérification si la position correspond à la dernière position de la personne
                            mysqli_data_seek($resultat_personne, 0); // Réinitialise l'itérateur
                            while ($personne = mysqli_fetch_assoc($resultat_personne)) {
                                if ($personne['X'] == $x && $personne['Y'] == $y) {
                                    $case_class = "case_bleue"; // Classe pour la personne
                                    break;
                                }
                            }
                            // Ajout des attributs data-x et data-y pour chaque case
                            echo "<td class='$case_class' data-x='$x' data-y='$y'></td>";
                        }
                        echo "</tr>";
                    }
                } elseif ($capteur == 'Ultrason') {
                    echo "<table class='salle-table-ultra'>";
                    echo "<tr><th>Zone 1</th><th></th><th>Zone 2</th><th></th><th>Zone 3</th><th></th><th>Zone 4</th></tr>";
                    echo "<tr class='salle-tr-ultra'>";
                    for ($x = 1; $x <= 7; $x++) {
                        $case_class = "case_vide_ultra";

                        // Vérification si la position correspond à un capteur
                        mysqli_data_seek($resultat_capteurs, 0); // Réinitialise l'itérateur
                        while ($capteur_row = mysqli_fetch_assoc($resultat_capteurs)) {
                            if ($capteur_row['Pos_X'] == $x) {
                                $case_class = "case_rouge_ultra"; // Classe pour les capteurs
                                break;
                            }
                        }

                        // Vérification si la position correspond à la dernière position de la personne
                        mysqli_data_seek($resultat_personne, 0); // Réinitialise l'itérateur
                        while ($personne = mysqli_fetch_assoc($resultat_personne)) {
                            if ($personne['X'] == $x) {
                                $case_class = "case_bleue_ultra"; // Classe pour la personne
                                break;
                            }
                        }
                        // Ajout de data-x pour chaque case ultrason
                        echo "<td class='$case_class' data-x='$x'></td>";
                    }
                    echo "</tr>";
                }
                echo "</table>";
            } else {
                echo "<p>Aucune salle trouvée avec ce nom.</p>";
            }
            echo "<br><br>";

            // Tableau des Légendes
            echo "<table class='tab-legende'>";
            echo "<caption>Légende</caption>";
            echo "<tr><th>Couleur</th><th>Correspondance</th></tr>";
            echo "<tr><td class='case_rouge_leg'></td><td>Capteurs</td></tr>";
            echo "<tr><td class='case_bleue_leg'></td><td>Dernière Position</td></tr>";
            echo "<tr><td class='case_grise_leg'></td><td>Positions Précédentes</td></tr>";
            echo "</table>";
        }
        ?>
        <br><br>
    </main>

    <!-- Pied de page -->
    <footer>
        Site réalisé dans le cadre de la SAE24<br>
        <a href="./mentions-legales.html">Mentions Légales</a><br>
    </footer>

    <!-- Inclusion des scripts JavaScript -->
    <script src="./scripts/script_actualisation.js"></script>
    <script src="./scripts/bouton_reset.js"></script>


    <?php
    mysqli_close($id_bd);
    ?>
</body>

</html>
