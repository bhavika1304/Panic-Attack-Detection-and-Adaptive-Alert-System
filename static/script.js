let currentStep = 0;

const steps = [
    { id: "step-base", action: handleBase },
    { id: "step-predict", action: handlePrediction },
    { id: "step-warning", action: handleEarlyWarning },
    { id: "step-alert", action: handlePersonalizedAlert },
    { id: "step-emergency", action: handleEmergencyContact },
    { id: "step-feedback", action: handleFeedback },
];

// Handle form submission
document.getElementById("input-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const heartRate = parseFloat(document.getElementById("heart-rate").value);
    document.getElementById("base-status").textContent = "Data submitted. Processing...";
    nextStep({ heart_rate: heartRate });
});

// Transition to the next step
function nextStep(data = {}) {
    if (currentStep >= steps.length) return; // Prevent out-of-bounds errors
    const step = steps[currentStep];
    document.querySelectorAll(".step").forEach((s) => s.classList.remove("active"));
    document.getElementById(step.id).classList.add("active");
    step.action(data);
    currentStep++;
}

// Handle Base Agent
function handleBase() {
    document.getElementById("base-status").textContent = "Waiting for user input...";
}

// Handle Prediction Agent
function handlePrediction(data) {
    const status = document.getElementById("predict-status");
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((result) => {
            if (result.panic_detected) {
                status.textContent = "Panic detected! Moving to Early Warning Agent...";
                setTimeout(() => nextStep(), 2000);
            } else {
                status.textContent = "No panic detected. Moving to Feedback Agent...";
                setTimeout(() => {
                    currentStep = steps.length - 1; // Skip to Feedback Agent
                    nextStep();
                }, 2000);
            }
        })
        .catch((error) => {
            console.error("Prediction Error:", error);
            status.textContent = "Error in prediction.";
        });
}

// Handle Early Warning Agent
function handleEarlyWarning() {
    const popup = document.getElementById("popup-warning");
    popup.style.display = "block";

    const timeout = setTimeout(() => {
        if (popup.style.display === "block") {
            popup.style.display = "none";
            handlePopupResponse("no_response", "warning");
        }
    }, 10000);

    document.querySelectorAll("#popup-warning button").forEach((btn) => {
        btn.addEventListener("click", () => clearTimeout(timeout));
    });
}

// Handle Personalized Alert System
function handlePersonalizedAlert() {
    const popup = document.getElementById("popup-alert");
    const music = document.getElementById("calming-music");
    popup.style.display = "block";
    music.play();

    const timeout = setTimeout(() => {
        if (popup.style.display === "block") {
            popup.style.display = "none";
            handlePopupResponse("no_response", "alert");
        }
    }, 20000);

    document.querySelectorAll("#popup-alert button").forEach((btn) => {
        btn.addEventListener("click", () => {
            clearTimeout(timeout);
            music.pause();
            music.currentTime = 0; // Reset music
        });
    });
}

// Handle Emergency Contact Agent
function handleEmergencyContact() {
    const status = document.getElementById("emergency-status");
    status.textContent = "Contacting emergency services...";
    fetch("/emergency_contact", { method: "POST" })
        .then(() => {
            status.textContent = "Emergency services contacted. Ending process.";
        })
        .catch((error) => {
            console.error("Emergency Contact Error:", error);
            status.textContent = "Failed to contact emergency services.";
        });
}

// Handle Feedback Agent
function handleFeedback() {
    const status = document.getElementById("feedback-status");
    status.textContent = "Awaiting feedback...";

    // Feedback is manually submitted
}

// Handle Popup Responses
function handlePopupResponse(response, context) {
    if (response === "yes") {
        currentStep = steps.length - 1; // Skip to Feedback Agent
        nextStep();
    } else if (response === "no_response") {
        nextStep();
    }
}

// Submit Feedback
function submitFeedback() {
    const feedbackText = document.getElementById("feedback-text").value;
    const status = document.getElementById("feedback-status");

    fetch("/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ feedback: feedbackText }),
    })
        .then(() => {
            status.textContent = "Feedback saved. Thank you!";
        })
        .catch((error) => {
            console.error("Feedback Error:", error);
            status.textContent = "Error saving feedback.";
        });
}
