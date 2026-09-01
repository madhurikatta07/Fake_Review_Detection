// loading spinner and flash message
document.addEventListener("DOMContentLoaded", function () {

    // Loading Spinner

    const form = document.getElementById("analyze-form");

    if (!form) {
        return;
    }

    form.addEventListener("submit", function () {

        const button = document.getElementById("submit-btn");

        const text = document.getElementById("btn-text");

        const loader = document.getElementById("btn-loader");

        button.disabled = true;

        text.style.display = "none";

        loader.style.display = "inline-flex";

    });

    // Flash Messages - Auto-dismiss with hover pause & smooth fade out
    const flashMessages = document.querySelectorAll(".flash-message");

    flashMessages.forEach(function (message) {
        let dismissTimeout;

        function startTimer(duration = 5000) {
            dismissTimeout = setTimeout(function () {
                fadeOutAndRemove(message);
            }, duration);
        }

        function clearTimer() {
            if (dismissTimeout) {
                clearTimeout(dismissTimeout);
            }
        }

        // Pause countdown on hover
        message.addEventListener("mouseenter", clearTimer);

        // Resume countdown with 3s delay on mouse leave
        message.addEventListener("mouseleave", function () {
            startTimer(3000);
        });

        // Start initial 5-second timer
        startTimer();
    });

    function fadeOutAndRemove(element) {
        if (!element.classList.contains("fade-out")) {
            element.classList.add("fade-out");
            // Wait for CSS transition (300ms) to complete before removing the element
            setTimeout(function () {
                element.remove();
            }, 300);
        }
    }
});


/* =====================================
   CONFIDENCE TREND CHART
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    const chartCanvas = document.getElementById("confidenceChart");

    // Make sure the chart exists
    if (!chartCanvas) {
        return;
    }

    fetch("/confidence-data")
        .then(response => {

            if (!response.ok) {
                throw new Error("Failed to load confidence data");
            }

            return response.json();
        })

        .then(data => {

            const labels = data.map(
                item => "Review " + item.id
            );

            const confidence = data.map(
                item => item.confidence
            );

            const ctx = chartCanvas.getContext("2d");

            new Chart(ctx, {

                type: "line",

                data: {

                    labels: labels,

                    datasets: [{
                        label: "Confidence (%)",

                        data: confidence,

                        tension: 0.3,

                        fill: false
                    }]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    scales: {

                        y: {

                            beginAtZero: true,

                            max: 100,

                            title: {
                                display: true,
                                text: "Confidence (%)"
                            }

                        },

                        x: {

                            title: {
                                display: true,
                                text: "Reviews"
                            }

                        }

                    }

                }

            });

        })

        .catch(error => {

            console.error(
                "Error loading confidence data:",
                error
            );

        });

});