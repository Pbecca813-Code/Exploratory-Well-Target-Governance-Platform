document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".workspace-card");

    cards.forEach(function(card) {

        card.addEventListener("click", function() {

            window.location.href = this.dataset.url;

        });

    });

});