/* ==========================================================================
   DermCare Clinical AI - Frontend JS Controller
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
    const dropzone = document.getElementById("dropzone");
    const fileInput = document.getElementById("file-input");
    const browseBtn = document.getElementById("browse-btn");
    const dropzonePrompt = document.getElementById("dropzone-prompt");
    const previewContainer = document.getElementById("preview-container");
    const imagePreview = document.getElementById("image-preview");
    const uploadControls = document.getElementById("upload-controls");
    const btnAnalyze = document.getElementById("btn-analyze");
    const btnReset = document.getElementById("btn-reset");
    const resultsDashboard = document.getElementById("results-dashboard");

    const predictedName = document.getElementById("predicted-name");
    const predictedCategory = document.getElementById("predicted-category");
    const predictedDesc = document.getElementById("predicted-desc");
    const confidenceChip = document.getElementById("confidence-chip");
    const probBars = document.getElementById("prob-bars");
    const immediateAdviceText = document.getElementById("immediate-advice-text");
    const riskBadge = document.getElementById("risk-badge");

    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const chatContainer = document.getElementById("chat-container");
    const chipBtns = document.querySelectorAll(".chip-btn");

    let currentFile = null;
    let currentPrediction = null;

    // File Selection Trigger
    browseBtn.addEventListener("click", () => fileInput.click());

    fileInput.addEventListener("change", function (e) {
        if (e.target.files && e.target.files[0]) {
            handleFileSelect(e.target.files[0]);
        }
    });

    // Drag and Drop Logic
    dropzone.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropzone.classList.add("dragover");
    });

    dropzone.addEventListener("dragleave", () => {
        dropzone.classList.remove("dragover");
    });

    dropzone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropzone.classList.remove("dragover");
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFileSelect(e.dataTransfer.files[0]);
        }
    });

    function handleFileSelect(file) {
        currentFile = file;
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            dropzonePrompt.classList.add("hidden");
            previewContainer.classList.remove("hidden");
            uploadControls.classList.remove("hidden");
        };
        reader.readAsDataURL(file);
    }

    btnReset.addEventListener("click", function () {
        currentFile = null;
        fileInput.value = "";
        imagePreview.src = "";
        dropzonePrompt.classList.remove("hidden");
        previewContainer.classList.add("hidden");
        uploadControls.classList.add("hidden");
        resultsDashboard.classList.add("hidden");
        currentPrediction = null;
    });

    // Run Vision Classification
    btnAnalyze.addEventListener("click", function () {
        if (!currentFile) return;

        btnAnalyze.disabled = true;
        btnAnalyze.textContent = "Analyzing Scan...";

        const formData = new FormData();
        formData.append("file", currentFile);

        fetch("/api/classify", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            btnAnalyze.disabled = false;
            btnAnalyze.textContent = "Run Vision Analysis";

            if (data.error) {
                alert("Error during classification: " + data.error);
                return;
            }

            renderPrediction(data);
        })
        .catch(err => {
            btnAnalyze.disabled = false;
            btnAnalyze.textContent = "Run Vision Analysis";
            console.error("Classification error:", err);
        });
    });

    function renderPrediction(data) {
        currentPrediction = data;
        predictedName.textContent = data.disease_name;
        predictedCategory.textContent = `Severity: ${data.severity} | Risk: ${data.risk_level}`;
        predictedDesc.textContent = data.description || "Dermatoscopic vision feature extraction completed.";
        confidenceChip.textContent = `${data.confidence}%`;

        // Risk Badge styling
        riskBadge.textContent = `${data.risk_level} Risk`;
        riskBadge.className = `risk-badge ${data.risk_level.toLowerCase()}`;

        // Immediate Medical Advice
        immediateAdviceText.textContent = data.immediate_advice || "Consult a specialist for clinical evaluation.";

        // Probability Bars
        probBars.innerHTML = "";
        if (data.top_3_predictions) {
            data.top_3_predictions.forEach(item => {
                const row = document.createElement("div");
                row.className = "prob-row";
                row.innerHTML = `
                    <div class="prob-labels">
                        <span>${item.name}</span>
                        <span>${item.probability}%</span>
                    </div>
                    <div class="prob-bar-bg">
                        <div class="prob-bar-fill" style="width: ${item.probability}%"></div>
                    </div>
                `;
                probBars.appendChild(row);
            });
        }

        resultsDashboard.classList.remove("hidden");
    }

    // Chat Assistant Form
    chatForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const msg = chatInput.value.trim();
        if (!msg) return;

        sendChatMessage(msg);
        chatInput.value = "";
    });

    // Chip prompt click handlers
    chipBtns.forEach(btn => {
        btn.addEventListener("click", function() {
            const query = this.getAttribute("data-query");
            if (query) {
                sendChatMessage(query);
            }
        });
    });

    function sendChatMessage(msg) {
        appendMessage("user", msg);

        const payload = {
            message: msg,
            predicted_class: currentPrediction ? currentPrediction.prediction_code : null
        };

        fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(data => {
            if (data.response) {
                appendMessage("assistant", data.response);
            } else if (data.error) {
                appendMessage("assistant", "Apologies, an error occurred: " + data.error);
            }
        })
        .catch(err => {
            console.error("Chat error:", err);
            appendMessage("assistant", "Unable to connect to RAG server. Please try again.");
        });
    }

    function appendMessage(sender, text) {
        const row = document.createElement("div");
        row.className = `chat-row ${sender === 'user' ? 'user-row' : 'assistant-row'}`;

        const avatar = document.createElement("div");
        avatar.className = "avatar";
        avatar.textContent = sender === 'user' ? "👤" : "🩺";

        const bubble = document.createElement("div");
        bubble.className = "msg-bubble";
        
        const senderName = document.createElement("div");
        senderName.className = "sender-name";
        senderName.textContent = sender === 'user' ? "You" : "Clinical Assistant";

        const msgText = document.createElement("div");
        msgText.className = "msg-text";
        msgText.innerHTML = text.replace(/\n/g, "<br>");

        bubble.appendChild(senderName);
        bubble.appendChild(msgText);

        row.appendChild(avatar);
        row.appendChild(bubble);

        chatContainer.appendChild(row);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});
