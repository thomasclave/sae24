<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAE24 - Groupe 31</title>

    <!--CSS links-->
    <link rel="stylesheet" href="./css/style.css">

    <!--Policies links-->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    
</head>
<body>
    <!--Navbar-->
    <nav class="navbar">
        <a class="nav-nom" href="./index.php">SAE24 - Groupe 31</a>
        <ul class="nav-links">
            <li class="active"><a href="./index.php">Accueil</a></li>
            <li><a href="./consultation.php">Consultation</a></li>
            <li><a href="./administration.php">Administration</a></li>
            <li><a href="./gestion-projet.html">Gestion de Projet</a></li>
            <li><a href="./mentions-legales.html">Mentions Légales</a></li>
        </ul>
     </nav>
     
     <!--Title-->
     <header>
     <h2>Accueil SAE24 - Groupe 31</h2>
     </header>

<main>

    <h2>Situation professionnelle</h2>
    <p>
    Exploiter des signaux émis par trois capteurs
    à ultrasons et réfléchis par une personne 
    <br><br>
    Exploiter un signal sonore (sinusoïdal) émis par
    un objet et reçu par trois microphones.
    <br><br>
    Estimer la position en (x,y) de l'objet dans
    une pièce à l'aide des deux approches
    <br><br>
    Présenter l'estimation de la position sur une
    interface dédiée
    <br><br>
    </p>


    <h2>Fonctionnalités du projet</h2>

    <p>
    Permettre à une personne de retrouver un objet en lui
faisant émettre un son.

    <br><br>
    Permettre de localiser une personne dans une pièce
via les capteurs ultrasons.
    <br><br>
    </p>
    

      
      


    <h2>Salles gérées</h2>
        <?php
        include("./script_bdd/mysql.php"); // Connect to the database
        
        // Query to get the managed rooms
        $query_rooms = "
        SELECT NomSalle, Bat
        FROM Salle
        ";

        $result_rooms = mysqli_query($id_bd, $query_rooms);

        if ($result_rooms && mysqli_num_rows($result_rooms) > 0) {
            echo "<table>";
            echo "<tr><th>Salle</th><th>Bâtiment</th></tr>";
            while ($room = mysqli_fetch_assoc($result_rooms)) {
                echo "<tr><td>" . $room['NomSalle'] . "</td><td>" . $room['Bat'] . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "<p>Aucune salle trouvée.</p>";
        }
        echo "<br><br>";
        // Close the database connection
        mysqli_close($id_bd);
        ?>

        



</main>

<!--Footer-->
<footer>
    Site réalisé dans le cadre de la SAE24<br>
    <a href="./mentions-legales.html">Mentions Légales</a><br>
</footer>

</body>
</html>
