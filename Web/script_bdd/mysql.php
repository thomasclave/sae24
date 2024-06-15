<?php
/* Connection Script to database SQL */

  $id_bd = mysqli_connect("localhost","g31","passg31","sae24")
    or die("Connexion au serveur et/ou à la base de données impossible");

  /* Character encoding management */
  mysqli_query($id_bd, "SET NAMES 'utf8'");

?>