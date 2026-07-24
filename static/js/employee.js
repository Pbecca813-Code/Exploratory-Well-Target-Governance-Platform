document.addEventListener("DOMContentLoaded", function () {

    const photoInput = document.getElementById("photoInput");
    const photoPreview = document.getElementById("photoPreview");

    if (photoInput && photoPreview) {

        photoInput.addEventListener("change", function () {

            const file = this.files[0];

            if (file) {

                const reader = new FileReader();

                reader.onload = function (e) {

                    photoPreview.src = e.target.result;

                };

                reader.readAsDataURL(file);

            }

        });

    }

});