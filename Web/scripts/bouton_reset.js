document.addEventListener("DOMContentLoaded", function() {
    // Ajout d'un gestionnaire d'événements pour le bouton de réinitialisation
    document.getElementById("reset-button").addEventListener("click", function() {
        // Récupère tous les éléments <td> du tableau
        var cases = document.querySelectorAll(".salle-table td.case_grise, .salle-table-ultra td.case_grise_ultra");

        // Parcours chaque case grise et la transforme en case vide
        cases.forEach(function(caseElement) {
            caseElement.className = caseElement.className.includes('ultra') ? "case_vide_ultra" : "case_vide";
        });
    });
});
