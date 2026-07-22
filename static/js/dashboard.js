const statusCanvas = document.getElementById("statusChart");
const documentCanvas = document.getElementById("documentChart");

/* ==============================
   TARGET STATUS CHART
============================== */

if (statusCanvas) {

    const draft = Number(statusCanvas.dataset.draft);
    const review = Number(statusCanvas.dataset.review);
    const validated = Number(statusCanvas.dataset.validated);
    const approved = Number(statusCanvas.dataset.approved);

    new Chart(statusCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Draft",
                "Review",
                "Validated",
                "Approved"
            ],

            datasets: [{

                data: [
                    draft,
                    review,
                    validated,
                    approved
                ],

                backgroundColor: [
                    "#2563EB",
                    "#F59E0B",
                    "#10B981",
                    "#8B5CF6"
                ],

                borderWidth: 2

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}

/* ==============================
   DOCUMENT CHART
============================== */

if (documentCanvas) {

    const documents = Number(documentCanvas.dataset.documents);

    new Chart(documentCanvas, {

        type: "bar",

        data: {

            labels: [

                "Uploaded Documents"

            ],

            datasets: [{

                label: "Documents",

                data: [

                    documents

                ],

                backgroundColor: "#2563EB"

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {

                    beginAtZero: true,

                    ticks: {

                        precision: 0

                    }

                }

            },

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}