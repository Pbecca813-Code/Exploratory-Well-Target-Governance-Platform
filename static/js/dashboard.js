const statusCanvas = document.getElementById("statusChart");
const documentCanvas = document.getElementById("documentChart");

if (statusCanvas) {
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
                data: [0, 0, 0, 0],
                backgroundColor: [
                    "#2563EB",
                    "#F59E0B",
                    "#10B981",
                    "#8B5CF6"
                ]
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 2,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}

if (documentCanvas) {
    new Chart(documentCanvas, {
        type: "line",
        data: {
            labels: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],
            datasets: [{
                label: "Documents",
                data: [0, 0, 0, 0, 0, 0],
                borderColor: "#2563EB",
                backgroundColor: "rgba(37,99,235,0.15)",
                fill: true,
                tension: 0.35
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 2,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}