<?php
include("./script_bdd/mysql.php");

// Vérification si des données ont été postées depuis le formulaire
if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
    $salle = $_POST["salle"];
    $capteur = $_POST["capteur"];

    // Requête pour récupérer les dimensions de la salle sélectionnée
    $requete_dimensions = "SELECT Longueur, Largeur FROM Salle WHERE NomSalle = '$salle'";
    $resultat_dimensions = mysqli_query($id_bd, $requete_dimensions);
    $row_dimensions = mysqli_fetch_assoc($resultat_dimensions);
    $longueur = $row_dimensions['Longueur'];
    $largeur = $row_dimensions['Largeur'];

    // Requête pour récupérer les positions des capteurs
    $requete_capteurs = "SELECT TypeCapt, Pos_X, Pos_Y FROM Capteur WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
    $resultat_capteurs = mysqli_query($id_bd, $requete_capteurs);

    // Requête pour récupérer la derniere position de la personne
    $requete_personne = "SELECT X, Y FROM Data WHERE NomSalle = '$salle' ORDER BY Date DESC, Time DESC LIMIT 1";
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
                    $selected = ($nomSalle == $salle) ? "selected" : "";
                    echo "<option value='$nomSalle' $selected>$nomSalle</option>";
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

        <br><br>

        <?php
        // Affichage des résultats si le formulaire a été soumis
        if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
            if ($resultat_capteurs && mysqli_num_rows($resultat_capteurs) > 0) {
                echo "<h2>Position des capteurs</h2>";
                echo "<table>";
                echo "<tr><th>Position X</th><th>Position Y</th></tr>";
                while ($capteur = mysqli_fetch_assoc($resultat_capteurs)) {
                    echo "<tr><td>" . $capteur['Pos_X'] . "</td><td>" . $capteur['Pos_Y'] . "</td></tr>";
                }
                echo "</table>";
                echo "<br><br>";
                echo "<h2>Dernière position de la personne</h2>";
                echo "<table>";
                echo "<tr><th>Position X</th><th>Position Y</th></tr>";
                while ($personne = mysqli_fetch_assoc($resultat_personne)) {
                    echo "<tr><td>" . $personne['X'] . "</td><td>" . $personne['Y'] . "</td></tr>";
                }
                echo "</table>";
                echo "<br><br>";
                echo "<h2>Dimensions de la salle</h2>";
                echo "<table>";
                echo "<tr><th>-</th><th>Valeur</th></tr>";
                echo "<tr><td>Longueur (X)</td><td>". $longueur ."</td></tr>";
                echo "<tr><td>Largeur (Y)</td><td>". $largeur."</td></tr>";
                echo "</table>";
                echo "<br><br>";
            } else {
                echo "<p>Aucun capteur de type $capteur trouvé dans la salle $salle.</p>";
            }
        }
        ?>

    </main>

    <!-- Pied de page -->
    <footer>
        Site réalisé dans le cadre de la SAE24<br>
        <a href="./mentions-legales.html">Mentions Légales</a><br>
    </footer>

    <?php
    mysqli_close($id_bd);
    ?>
</body>

</html>