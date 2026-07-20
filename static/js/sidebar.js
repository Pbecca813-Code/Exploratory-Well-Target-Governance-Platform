document.addEventListener("DOMContentLoaded", function () {

    const dropdowns = document.querySelectorAll(".sidebar-dropdown");

    // Restore previously opened section
    const savedIndex = localStorage.getItem("sidebar-open");

    if (savedIndex !== null && dropdowns[savedIndex]) {

        dropdowns[savedIndex].classList.add("active");

        const menu = dropdowns[savedIndex].nextElementSibling;

        if (menu) {
            menu.style.display = "block";
        }

    }

    dropdowns.forEach((button, index) => {

        button.addEventListener("click", function () {

            dropdowns.forEach((otherButton, otherIndex) => {

                const otherMenu = otherButton.nextElementSibling;

                if (otherIndex !== index) {

                    otherButton.classList.remove("active");

                    if (otherMenu) {
                        otherMenu.style.display = "none";
                    }

                }

            });

            const menu = this.nextElementSibling;

            if (!menu) return;

            if (menu.style.display === "block") {

                menu.style.display = "none";

                this.classList.remove("active");

                localStorage.removeItem("sidebar-open");

            } else {

                menu.style.display = "block";

                this.classList.add("active");

                localStorage.setItem("sidebar-open", index);

            }

        });

    });

});