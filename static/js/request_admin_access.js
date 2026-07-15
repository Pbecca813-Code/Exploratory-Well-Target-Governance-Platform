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