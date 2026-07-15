document.addEventListener("DOMContentLoaded", () => {

    setupUpload(
        "id_profile_photo",
        "profile-preview",
        "profile-placeholder",
        "profile-actions"
    );

    setupUpload(
        "id_identification_document",
        "document-preview",
        "document-placeholder",
        "document-actions"
    );

});

function setupUpload(inputId, previewId, placeholderId, actionsId){

    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    const placeholder = document.getElementById(placeholderId);
    const actions = document.getElementById(actionsId);

    if(!input) return;

    input.addEventListener("change", function(){

        if(!this.files.length){

            preview.style.display="none";
            placeholder.style.display="flex";
            actions.style.display="none";

            return;

        }

        const file=this.files[0];

        if(file.type.startsWith("image")){

            const reader=new FileReader();

            reader.onload=function(e){

                preview.src=e.target.result;

                preview.style.display="block";
                placeholder.style.display="none";
                actions.style.display="flex";

            };

            reader.readAsDataURL(file);

        }else{

            placeholder.innerHTML="📄";

            preview.style.display="none";
            placeholder.style.display="flex";
            actions.style.display="flex";

        }

    });

}

const documentInput = document.getElementById("id_identification_document");
const profileInput = document.getElementById("id_profile_photo");

documentInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        document.getElementById("document-name").textContent =
            "✓ " + this.files[0].name;

    }

});

profileInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        document.getElementById("photo-name").textContent =
            "✓ " + this.files[0].name;

        const reader = new FileReader();

        reader.onload = function (e) {

            const avatar = document.getElementById("header-profile-preview");
            const placeholder = document.getElementById("header-profile-placeholder");

            avatar.src = e.target.result;
            avatar.style.display = "block";
            placeholder.style.display = "none";

        };

        reader.readAsDataURL(profileInput.files[0]);

    }

});

document.getElementById("view-document-link").onclick = function(e){

    e.preventDefault();

    if(documentInput.files.length){

        window.open(
            URL.createObjectURL(documentInput.files[0]),
            "_blank"
        );

    }

};

document.getElementById("download-document-link").onclick = function(e){

    e.preventDefault();

    if(documentInput.files.length){

        const a = document.createElement("a");

        a.href = URL.createObjectURL(documentInput.files[0]);

        a.download = documentInput.files[0].name;

        a.click();

    }

};

document.getElementById("remove-document-link").onclick = function(e){

    e.preventDefault();

    documentInput.value = "";

    document.getElementById("document-name").textContent =
        "No document selected";

};

document.getElementById("change-photo-link").onclick = function(e){

    e.preventDefault();

    profileInput.click();

};

document.getElementById("remove-photo-link").onclick = function(e){

    e.preventDefault();

    profileInput.value = "";

    document.getElementById("photo-name").textContent =
        "No photo selected";

    document.getElementById("header-profile-preview").style.display =
        "none";

    document.getElementById("header-profile-placeholder").style.display =
        "flex";

};

document.getElementById("position-photo-link").onclick = function(e){

    e.preventDefault();

    alert("Photo positioning will be available in Version 2.");

};