document.addEventListener("DOMContentLoaded", function () {

    const photoInput = document.getElementById("id_profile_photo");
    const photoPreview = document.getElementById("photo-preview");
    const photoPlaceholder = document.getElementById("photo-placeholder");

    if (!photoInput) return;

    photoInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) {

            photoPreview.style.display = "none";
            photoPlaceholder.style.display = "block";
            return;

        }

        const reader = new FileReader();

        reader.onload = function (e) {

            photoPreview.src = e.target.result;
            photoPreview.style.display = "block";
            photoPlaceholder.style.display = "none";

        };

        reader.readAsDataURL(file);

    });

});