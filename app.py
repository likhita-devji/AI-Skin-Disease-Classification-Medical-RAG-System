import os
import json
import uuid
import traceback
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload limit

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Lazy instance holders for AI components
_classifier = None
_rag_engine = None

def get_classifier():
    global _classifier
    if _classifier is None:
        print("[App Setup] Loading Vision Classifier model...")
        from models.classifier import SkinDiseaseClassifier
        _classifier = SkinDiseaseClassifier(
            model_path=os.path.join(BASE_DIR, "models", "skin_disease_classifier.keras"),
            class_names_path=os.path.join(BASE_DIR, "class_names.json")
        )
    return _classifier

def get_rag_engine():
    global _rag_engine
    if _rag_engine is None:
        print("[App Setup] Loading Medical RAG Engine & Vector DB...")
        from rag.rag_engine import SkinDiseaseRAGEngine
        _rag_engine = SkinDiseaseRAGEngine()
    return _rag_engine

def is_allowed_file(filename: str) -> bool:
    """Validate image file extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# -------------------------------------------------------------
# Web Routes
# -------------------------------------------------------------
@app.route("/")
def index():
    """Render main web dashboard."""
    return render_template("index.html")

@app.route("/uploads/<path:filename>")
def serve_upload(filename):
    """Serve uploaded images to frontend preview."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# -------------------------------------------------------------
# REST API Endpoints
# -------------------------------------------------------------
@app.route("/api/health", methods=["GET"])
def health_check():
    """System health check endpoint."""
    try:
        clf = get_classifier()
        return jsonify({
            "status": "online",
            "service": "Skin Disease Classifier & RAG Assistant",
            "supported_classes": clf.class_keys
        })
    except Exception as e:
        return jsonify({"status": "degraded", "error": str(e)}), 500

@app.route("/api/classify", methods=["POST"])
def classify():
    """
    POST Image Upload -> CNN Disease Classification -> Grounded RAG Summary.
    """
    if "file" not in request.files:
        return jsonify({"success": False, "error": "No file uploaded in request."}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"success": False, "error": "No file selected."}), 400

    if not is_allowed_file(file.filename):
        return jsonify({"success": False, "error": "Invalid file extension. Allowed: PNG, JPG, JPEG, WEBP."}), 400

    try:
        # Save file securely
        ext = file.filename.rsplit(".", 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
        file.save(save_path)

        # Run model inference
        clf = get_classifier()
        prediction = clf.predict(save_path)

        # Fetch grounded RAG medical summary
        rag = get_rag_engine()
        rag_summary = rag.generate_response(
            user_query=f"Medical treatment guidelines and cure options for {prediction['disease_name']}",
            predicted_disease_code=prediction["prediction_code"],
            disease_info=prediction
        )

        return jsonify({
            "success": True,
            "image_url": f"/uploads/{unique_filename}",
            "prediction": prediction,
            "rag_clinical_summary": rag_summary
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": f"Classification failed: {str(e)}"}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    """
    POST User Query -> Vector DB Context Search -> Grounded Answer.
    """
    data = request.get_json() or {}
    user_query = data.get("query", "").strip()
    disease_code = data.get("disease_code", "")

    if not user_query:
        return jsonify({"success": False, "error": "Please enter a valid medical question."}), 400

    try:
        clf = get_classifier()
        disease_info = clf.class_info.get(disease_code, {}) if disease_code else {}

        rag = get_rag_engine()
        rag_response = rag.generate_response(
            user_query=user_query,
            predicted_disease_code=disease_code,
            disease_info=disease_info
        )

        return jsonify({
            "success": True,
            "query": user_query,
            "response": rag_response["response"],
            "grounded_sources": rag_response.get("grounded_sources", [])
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": f"Chat processing error: {str(e)}"}), 500

@app.route("/api/knowledge-base", methods=["GET"])
def list_knowledge_base():
    """Returns list of indexed document sources."""
    try:
        rag = get_rag_engine()
        docs = rag.vector_store.documents
        sources = {}
        for d in docs:
            src = d['source']
            if src not in sources:
                sources[src] = {"source": src, "title": d['title'], "chunks": 0}
            sources[src]["chunks"] += 1

        return jsonify({
            "success": True,
            "documents": list(sources.values())
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n==========================================================")
    print(f" Starting Skin Disease Classifier Server on port {port}")
    print(f" Access app at: http://localhost:{port}")
    print(f"==========================================================\n")
    app.run(host="0.0.0.0", port=port, debug=True)
