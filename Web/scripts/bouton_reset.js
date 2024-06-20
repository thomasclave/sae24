document.addEventListener("DOMContentLoaded", function() {
    // Adding an event handler for the reset button
    document.getElementById("reset-button").addEventListener("click", function() {
        // Get all the <td> elements of the table
        var cases = document.querySelectorAll(".salle-table td.case_grise, .salle-table-ultra td.case_grise_ultra");

        // Iterate through each gray case and transform it into an empty case
        cases.forEach(function(caseElement) {
            caseElement.className = caseElement.className.includes('ultra') ? "case_vide_ultra" : "case_vide";
        });

        // Send a request to the script to reset the database
        fetch('./scripts/script_btn_reset.php', {
            method: 'GET', 
        })
    });
});
