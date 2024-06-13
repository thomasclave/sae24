<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAE24</title>

    <!--CSS links-->
    <link rel="stylesheet" href="./css/style.css">

    <!--Policies links-->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    
</head>
<body>
    <!--Navbar-->
    <nav class="navbar">
        <a class="nav-nom" href="./index.php">SAE24</a>
        <ul class="nav-links">
            <li class="active"><a href="./index.php">Accueil</a></li>
            <li><a href="./consultation.php">Consultation</a></li>
            <li><a href="./mentions-legales.html">Mentions Légales</a></li>
        </ul>
     </nav>
     
     <!--Title-->
     <header>
     <h2>Accueil SAE24</h2>
     </header>

<main>

    <h2>Salles gérées</h2>
        <?php
        include 'mysql.php'; // Connect to the database
        
        // Query to get the managed rooms
        $query_rooms = "
        SELECT Nom, Bat
        FROM Salle
        ";

        $result_rooms = mysqli_query($id_bd, $query_rooms);

        if ($result_rooms && mysqli_num_rows($result_rooms) > 0) {
            echo "<table>";
            echo "<tr><th>Salle</th><th>Bâtiment</th></tr>";
            while ($room = mysqli_fetch_assoc($result_rooms)) {
                echo "<tr><td>" . $room['Nom'] . "</td><td>" . $room['Bat'] . "</td></tr>";
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
