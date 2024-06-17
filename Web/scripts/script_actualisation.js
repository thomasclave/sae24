// Attend que le DOM soit chargé
document.addEventListener("DOMContentLoaded", function() {
    // Fonction pour actualiser les données toutes les secondes
    setInterval(actualiserPositions, 1000); // Actualisation toutes les 1000 ms (1 seconde)

    // Fonction pour actualiser les positions
    function actualiserPositions() {
        // Effectue une requête AJAX pour récupérer la dernière position de la personne
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "./scripts/script_actualisation.php", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                // Réponse reçue, traitement des données
                var data = JSON.parse(xhr.responseText);
                mettreAJourTableaux(data);
            }
        };
        xhr.send();
    }

    // Fonction pour mettre à jour les tableaux avec les nouvelles données
    function mettreAJourTableaux(data) {
        mettreAJourTableauSon(data);
        mettreAJourTableauUltrason(data);
    }

    // Fonction pour mettre à jour le tableau Son avec les nouvelles données
    function mettreAJourTableauSon(data) {
        var casesSon = document.querySelectorAll(".salle-table td");

        casesSon.forEach(function(caseElement) {
            var x = caseElement.dataset.x;
            var y = caseElement.dataset.y;

            if (x == data.X && y == data.Y) {
                caseElement.classList.add("case_bleue");
            } else if (caseElement.classList.contains("case_bleue")) {
                    caseElement.classList.remove("case_bleue");
                    caseElement.classList.add("case_aqua");
            } else if (caseElement.classList.contains("case_aqua")) {
                caseElement.classList.remove("case_bleue");
                caseElement.classList.add("case_grise");
            } else {
                caseElement.classList.remove("case_bleue");
                caseElement.classList.add("case_vide");
            }
        });
    }

    // Fonction pour mettre à jour le tableau Ultrason avec les nouvelles données
    function mettreAJourTableauUltrason(data) {
        var casesUltrason = document.querySelectorAll(".salle-table-ultra td");

        casesUltrason.forEach(function(caseElement) {
            var x = caseElement.dataset.x;

            if (x == data.X) {
                caseElement.classList.add("case_bleue_ultra");
            } else if (caseElement.classList.contains("case_bleue_ultra")) {
                    caseElement.classList.remove("case_bleue_ultra");
                    caseElement.classList.add("case_vide_ultra");
            }else{
                caseElement.classList.remove("case_bleue_ultra");
                caseElement.classList.add("case_vide_ultra");
            }
        });
    }
});
