// Wait for the DOM to be loaded
document.addEventListener("DOMContentLoaded", function() {
    // Function to update the data every second
    setInterval(actualiserPositions, 1000); // Refresh every 1000 ms (1 second)

    // Function to update the positions
    function actualiserPositions() {
        // Performs an AJAX request to retrieve the latest position of the person
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "./scripts/script_actualisation.php", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                // Response received, data processing

                var data = JSON.parse(xhr.responseText);
                mettreAJourTableaux(data);
            }
        };
        xhr.send();
    }

    // Function to update the tables with the new data
    function mettreAJourTableaux(data) {
        mettreAJourTableauSon(data);
        mettreAJourTableauUltrason(data);
    }

    // Function to update the Son table with the new data
    function mettreAJourTableauSon(data) {
        var casesSon = document.querySelectorAll(".salle-table td");

        casesSon.forEach(function(caseElement) {
            var x = caseElement.dataset.x;
            var y = caseElement.dataset.y;

            if (x == data.X && y == data.Y) {
                caseElement.classList.add("case_bleue");
            } else if (caseElement.classList.contains("case_bleue")) {
                caseElement.classList.remove("case_bleue");
                caseElement.classList.add("case_grise");
            } else {
                caseElement.classList.remove("case_bleue");
                caseElement.classList.add("case_vide");
            }
        });
    }

    // Function to update the Ultrason table with the new data
    function mettreAJourTableauUltrason(data) {
        var casesUltrason = document.querySelectorAll(".salle-table-ultra td");

        casesUltrason.forEach(function(caseElement) {
            var x = caseElement.dataset.x;

            if (x == data.X) {
                caseElement.classList.add("case_bleue_ultra");
            } else {
                caseElement.classList.remove("case_bleue_ultra");
                caseElement.classList.add("case_vide_ultra");
            }
        });
    }
});
