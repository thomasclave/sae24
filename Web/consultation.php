<?php
include("mysql.php");

// Récupération des noms de salles avec leurs longueurs et largeurs
$requete_salles = "SELECT NomSalle, Longueur, Largeur FROM Salle";
$resultat_salles = mysqli_query($id_bd, $requete_salles);

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
                    $nomSalle = $row['NomSalle'];
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
