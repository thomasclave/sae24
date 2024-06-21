<?php
include("./script_bdd/mysql.php");

// PART FOR THE ROOM ADDITION
// Check if data has been posted from the Room form
if (isset($_POST["NomSalle"]) && isset($_POST["Bat"]) && isset($_POST["Longueur"]) && isset($_POST["Largeur"])) {
    $salle = $_POST["NomSalle"];
    $bat = $_POST["Bat"];
    $longueur = $_POST["Longueur"];
    $largeur = $_POST["Largeur"];

    $requete_salle = "INSERT INTO `Salle` (`NomSalle`, `Bat`, `Longueur`, `Largeur`) VALUES ('$salle', '$bat', '$longueur', '$largeur');";
    $resultat_salle = mysqli_query($id_bd, $requete_salle);

    if ($resultat_salle) {
        $confirmation_message = "Salle ajoutée avec succès.";
    } else {
        $confirmation_message = "Erreur lors de l'ajout de la salle.";
    }

//PART FOR THE CAPTOR ADDITION
} elseif (isset($_POST["IDcapteur"]) && isset($_POST["TypeCapt"]) && isset($_POST["NomSalleCapt"]) && isset($_POST["Pos_X"]) && isset($_POST["Pos_Y"]) ) { // Check if data has been posted from the Room form
    $IDcapteur = $_POST["IDcapteur"];
    $TypeCapt = $_POST["TypeCapt"];
    $NomSalleCapt = $_POST["NomSalleCapt"];
    $Pos_X = $_POST["Pos_X"];
    $Pos_Y = $_POST["Pos_Y"];

    $requete_capt_salle = "INSERT INTO `Capteur` (`IDcapteur`, `TypeCapt`, `NomSalle`, `Pos_X`, `Pos_Y`) VALUES ('$IDcapteur', '$TypeCapt', '$NomSalleCapt', '$Pos_X', '$Pos_Y');";
    $resultat_capt_salle = mysqli_query($id_bd, $requete_capt_salle);
    echo $requete_capt_salle;

    if ($resultat_capt_salle) {
        $confirmation_message = "Capteur ajouté avec succès.";
    } else {
        $confirmation_message = "Erreur lors de l'ajout du capteur.";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAE24 - Consultation</title>

    <!-- CSS Links -->
    <link rel="stylesheet" href="./css/style.css">

    <!-- Font Links -->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
</head>

<body>
    <!-- Navigation Bar -->
    <nav class="navbar">
        <a class="nav-nom" href="./index.php">SAE24 - Groupe 31</a>
        <ul class="nav-links">
            <li><a href="./index.php">Accueil</a></li>
            <li><a href="./consultation.php">Consultation</a></li>
            <li class="active"><a href="./administration.php">Administration</a></li>
            <li><a href="./gestion-projet.html">Gestion de Projet</a></li>
            <li><a href="./mentions-legales.html">Mentions Légales</a></li>
        </ul>
    </nav>

    <!-- Title -->
    <header>
        <h2>Administration</h2>
    </header>

    <main>

        <?php if (!empty($confirmation_message)): ?>
            <div class="confirmation-message">
                <?php echo $confirmation_message; ?>
            </div>
        <?php endif; ?>

        
        <h3>Ajouter une Salle</h3>
        <form action="administration.php" method="POST">
            <label for="Defsalle">Définir le Nom de la salle : </label>
                <input type="text" name="NomSalle" required>
                <br><br>
            <label for="Defbat">Définir le Bâtiment :</label>
                <input type="text" name="Bat" required>
                <br><br>
            <label for="DefX">Définir la Longueur de la salle en "cases" (X) :</label>
                <input type="number" name="Longueur" inputmode='numeric' required>
                <br><br>
            <label for="DefY">Définir la Largeur de la salle en "cases" (Y) :</label>
                <input type="number" name="Largeur" inputmode='numeric' required>
                <br><br>
            <input type="submit" value="Ajouter la Salle">
        </form>

        <h3>Ajouter un Capteur son</h3>
        <form action="administration.php" method="POST">
            <label for="DefIDCAPT">Définir l'ID du capteur :</label>
                <input type="number" name="IDcapteur" inputmode='numeric' required>
                <br><br>

            <label for="capteur">Type de capteur :</label>
                <input type="text" name="TypeCapt" value="Son" required readonly>
                <br><br>


            <label for="Defcaptsalle">Sélectionnez une salle :</label>
            <select name="NomSalleCapt" id="salle" required>
                <option value="">Choisissez une salle</option>
                <?php
                // Display room selection options
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

            <label for="DefPosX">Définir la position X du capteur :</label>
                <input type="number" name="Pos_X" inputmode='numeric' required>
                <br><br>
            <label for="DefPosY">Définir la position Y du capteur :</label>
                <input type="number" name="Pos_Y" inputmode='numeric' required>
                <br><br>
            

            <input type="submit" value="Ajouter un capteur">
        </form>
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
