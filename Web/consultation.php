<?php
include("mysql.php");

// Récupération des noms de salles avec leurs longueurs et largeurs
$requete_salles = "SELECT Nom, Longueur, Largeur FROM Salle";
$resultat_salles = mysqli_query($id_bd, $requete_salles);

if (!$resultat_salles) {
    die("Erreur lors de l'exécution de la requête: " . mysqli_error($id_bd));
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAE24</title>

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
                while ($row = mysqli_fetch_assoc($resultat_salles)) {
                    $nomSalle = $row['Nom'];
                    echo "<option value='$nomSalle'>$nomSalle</option>";
                }
                ?>
            </select>
            <br><br>

            <label for="capteur">Sélectionnez un type de capteur :</label>
            <select name="capteur" id="capteur" required>
                <option value="Son">Son</option>
                <option value="UltraSon">UltraSon</option>
            </select>
            <br><br>

            <input type="submit" value="Consulter">
        </form>

        <!-- Affichage du tableau uniquement si le formulaire a été soumis -->
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["salle"]) && isset($_POST["capteur"])) {
            // Récupération de la salle sélectionnée
            $salle = $_POST["salle"];
            $capteur = $_POST["capteur"];

            // Récupération de la longueur et largeur de la salle depuis la base de données
            $requete_info_salle = "SELECT Longueur, Largeur FROM Salle WHERE Nom = '$salle'";
            $resultat_info_salle = mysqli_query($id_bd, $requete_info_salle);

            if (!$resultat_info_salle) {
                die("Erreur lors de l'exécution de la requête: " . mysqli_error($id_bd));
            }

            // Vérification si la salle existe
            if (mysqli_num_rows($resultat_info_salle) > 0) {
                $row_salle = mysqli_fetch_assoc($resultat_info_salle);
                $longueur = $row_salle['Longueur'];
                $largeur = $row_salle['Largeur'];

                // Construction du tableau en fonction du type de capteur
                echo "<h3>Résultats pour la salle $salle avec le capteur $capteur</h3>";
                if ($capteur == "Son") {
                    echo "<table class='Damier' border='1'>";
                    for ($i = 1; $i <= $largeur; $i++) {
                        echo "<tr>";
                        for ($j = 1; $j <= $longueur; $j++) {
                            echo "<td id='S$i-$j'>-</td>";
                        }
                        echo "</tr>";
                    }
                    echo "</table>";
                } elseif ($capteur == "UltraSon") {
                    // Tableau spécifique pour UltraSon (1 ligne x 4 colonnes)
                    echo "<table class='Damier_droit' border='1'>";
                    echo "<tr>";
                        echo "<td id='U1-1'>-</td>";
                        echo "<td id='U1-2'>-</td>";
                        echo "<td id='U1-3'>-</td>";
                        echo "<td id='U1-4'>-</td>";
                    echo "</tr>";
                    echo "</table>";
                }
            } else {
                echo "<p>Aucune information trouvée pour la salle sélectionnée.</p>";
            }
        }

        
        ?>

        <br><br>
    </main>

    <!-- Pied de page -->
    <footer>
        Site réalisé dans le cadre de la SAE24<br>
        <a href="./mentions-legales.html">Mentions Légales</a><br>
    </footer>

</body>

</html>

<?php
mysqli_close($id_bd);
?>
