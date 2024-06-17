<?php
include("./script_bdd/mysql.php");

//checking if data has been posted from the form
if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
    //store the result of the form in variables
    $salle = $_POST["salle"];
    $capteur = $_POST["capteur"];

    //sql query to retrieve the dimensions of the selected room 
    
    $requete_dimensions = "SELECT Longueur, Largeur FROM Salle WHERE NomSalle = '$salle'";
    //execute the query
    $resultat_dimensions = mysqli_query($id_bd, $requete_dimensions);
    $row_dimensions = mysqli_fetch_assoc($resultat_dimensions);
    //storing the dimensions in variables
    $longueur = $row_dimensions['Longueur'];
    $largeur = $row_dimensions['Largeur'];

    // sql query to retrieve the position of the sensors
    $requete_capteurs = "SELECT TypeCapt, Pos_X, Pos_Y FROM Capteur WHERE NomSalle = '$salle' AND TypeCapt = '$capteur'";
    $resultat_capteurs = mysqli_query($id_bd, $requete_capteurs);

    // sql query to retreive the position of the person
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

    <!-- CSS link -->
    <link rel="stylesheet" href="./css/style.css">

    <!-- Fonts link -->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
</head>

<body>
    <!-- Navbar -->
    <nav class="navbar">
        <a class="nav-nom" href="./index.php">SAE24</a>
        <ul class="nav-links">
            <li><a href="./index.php">Accueil</a></li>
            <li class="active"><a href="./consultation.php">Consultation</a></li>
            <li><a href="./mentions-legales.html">Mentions Légales</a></li>
        </ul>
    </nav>

    <!-- Title-->
    <header>
        <h2>Consultation</h2>
    </header>

    <main>
        <form action="consultation.php" method="POST">
            <label for="salle">Sélectionnez une salle :</label>
            <select name="salle" id="salle" required>
                <option value="">Choisissez une salle</option>
                <?php
                // Display room selection options
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
                <option value="UltraSon">Ultrason</option>
            </select>
            <br><br>

            <input type="submit" value="Consulter">
        </form>

        <br><br>

        <?php
        if (isset($_POST["salle"]) && isset($_POST["capteur"])) {
            if ($resultat_dimensions && mysqli_num_rows($resultat_dimensions) > 0) {

            // Table to display the positions of the sensors/person. 
            echo "<h2>Positions dans la salle</h2>";
            echo "<table class='salle-table'>";
            // Display empty boxes according to the dimensions of the room
            for ($y = 1; $y <= $largeur; $y++) {
                echo "<tr>";
                for ($x = 1; $x <= $longueur; $x++) {
                $case_class = "case_vide";
                // Checking if the position corresponds to a sensor
                mysqli_data_seek($resultat_capteurs, 0); // Resets the iterator
                while ($capteur = mysqli_fetch_assoc($resultat_capteurs)) {
                    if ($capteur['Pos_X'] == $x && $capteur['Pos_Y'] == $y) {
                        $case_class = "case_rouge"; // special CSS class for the sensors boxes
                        break;
                    }
                }

                // Checking if the position matches the person's last position
                mysqli_data_seek($resultat_personne, 0); // Resets the iterator
                while ($personne = mysqli_fetch_assoc($resultat_personne)) {
                    if ($personne['X'] == $x && $personne['Y'] == $y) {
                        $case_class = "case_bleue"; // special CSS class for the sensors boxes
                        break;
                    }
                }
                echo "<td class='$case_class'></td>";
            }
            echo "</tr>";
        }
        echo "</table>";
        } else {
            echo "<p>Aucune salle trouvée avec ce nom.</p>";
            }
        }
        ?>
    <br><br>

    </main>

    <!-- Footer -->
    <footer>
        Site réalisé dans le cadre de la SAE24<br>
        <a href="./mentions-legales.html">Mentions Légales</a><br>
    </footer>

    <?php
    mysqli_close($id_bd);
    ?>
</body>

</html>