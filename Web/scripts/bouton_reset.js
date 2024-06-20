document.addEventListener("DOMContentLoaded", function() {
    // Adding an event handler for the reset button
    document.getElementById("reset-button").addEventListener("click", function() {
        // Get all the <td> elements of the table
        var cases = document.querySelectorAll(".salle-table td.case_grise, .salle-table-ultra td.case_grise_ultra");

        // Iterate through each gray case and transform it into an empty case
        cases.forEach(function(caseElement) {
            caseElement.className = caseElement.className.includes('ultra') ? "case_vide_ultra" : "case_vide";
        });
        // Effectuer une requête AJAX pour réinitialiser les positions dans la BD
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "./scripts/script_btn_reset.php", true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log("Positions réinitialisées avec succès");
                // Réponse de la requête AJAX réussie, vous pouvez effectuer des actions supplémentaires ici si nécessaire
            } else {
                console.error("Erreur lors de la réinitialisation des positions");
            }
        };
        xhr.onerror = function() {
            console.error("Erreur de réseau ou autre lors de la réinitialisation des positions");
        };
        xhr.send();
    });
});
