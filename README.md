# AI Skin Disease Classification & Medical RAG System

An end-to-end Flask-based AI application that classifies skin disease images using EfficientNet (TensorFlow) and provides grounded medical guidance using RAG (Retrieval-Augmented Generation).

```
Dataset Link - https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000 (HAM10000 Dataset)
```

```
Model Link - https://github.com/likhita-devji/AI-Skin-Disease-Classification-Medical-RAG-System
```

## 🔹 System Architecture
The application utilizes a modular AI pipeline:
- **Vision Pipeline**: Processes image uploads through a TensorFlow CNN (EfficientNetB0) to identify 7 specific skin disease classes.
- **RAG Pipeline**: Uses LangChain and ChromaDB to retrieve context from trusted medical PDFs.
- **Inference Engine**: Generates safe, non-hallucinated responses via a local Ollama LLM.

## 🔹 System Architecture Overview
![AI Skin Disease Classification Medical RAG System Architecture](readme_images/system_architecture_infographic.png)

## 🔹 CNN Based Skin Disease Classification
![CNN-Based Skin Disease Classification Flow](readme_images/classification_flow_infographic.png)

## 🔹 Medical RAG Pipeline Architecture
![Medical RAG Pipeline Architecture](readme_images/medical_rag_pipeline_infographic.png)

---

## 🔹 Technology Stack

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF4F00?style=for-the-badge&logo=databricks&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)

| Architectural Layer | Technology & Libraries | Specialized Role & Description |
| :--- | :--- | :--- |
| **Frontend UI** | HTML5, CSS3, JavaScript (ES6+) | Glassmorphic Dashboard, Drag-and-Drop Image Uploader, Dynamic Medical RAG Modal & Micro-animations |
| **Backend REST API** | Flask, Flask-CORS | Asynchronous API Services, Request Routing, File Upload Processing & Pipeline Orchestration |
| **Deep Learning & CV** | TensorFlow, Keras, OpenCV, PIL | EfficientNetB0 Transfer Learning CNN for high-accuracy skin disease image classification |
| **RAG Pipeline Engine** | LangChain, PyPDF, Markdown | Medical document parsing, recursive text splitting, prompt engineering & context synthesis |
| **Vector Embeddings** | Sentence-Transformers (`all-MiniLM-L6-v2`) | High-dimensional dense semantic embedding generation for clinical literature |
| **Vector Database** | ChromaDB | Persistent HNSW indexing, similarity search & top-K context retrieval |
| **LLM & Local Inference** | Ollama (`llama3` / `llama-medicine`) | Local privacy-preserving LLM inference + Grounded Fallback Synthesis Engine with treatment protocols |
| **Data Science & Metrics** | Pandas, NumPy, Scikit-Learn | HAM10000 dataset preprocessing, class weight calculation, confusion matrices & model evaluation |
| **DevOps & Containerization**| Docker, Docker Compose | Microservice isolation, cross-platform portability, persistent volume mounts & host network bridging |

---

## 🔹 Supported Skin Disease Classes
- Actinic_Keratoses (akiec)
- Basal_Cell_Carcinoma (bcc)
- Benign_Keratosis (bkl)
- Dermatofibroma (df)
- Melanoma (mel)
- Melanocytic_Nevi (nv)
- Vascular_Lesions (vasc)

---

## 🔹 Project Structure
```
.
├── app.py                         # Main Flask Backend
├── Dockerfile                     # Container Configuration
├── skin_disease_classifier.keras  # Trained CNN Model
├── class_names.json               # Skin Disease Label Mapping
├── download_dataset.py            # Dataset Downloader Utility
├── requirements.txt               # Dependencies
├── models/
│   ├── classifier.py              # CNN Model Inference Engine
│   └── train_model.py             # EfficientNet Training Script
├── rag/
│   ├── vector_store.py            # ChromaDB Vector Store (PDF & MD)
│   └── rag_engine.py              # RAG Query & LLM Engine
├── medical_knowledge_db/          # Trusted Medical PDFs & Reference Guides
│   ├── skin_diseases_medical_guide.pdf
│   ├── melanoma.md
│   ├── basal_cell_carcinoma.md
│   └── ...
├── readme_images/                 # Infographic Diagrams for README
│   ├── system_architecture_infographic.png
│   ├── classification_flow_infographic.png
│   └── medical_rag_pipeline_infographic.png
├── chroma_db/                     # Persistent Vector Store
├── uploads/                       # User Uploaded Images
├── templates/                     # Frontend UI (Jinja2)
└── static/                        # CSS & JS Frontend Assets
    ├── css/style.css
    └── js/main.js
```

---

## 🔹 Deployment (Docker)
This project is containerized for production-ready consistency. It uses a Hybrid Architecture where the application logic is isolated in Docker while connecting to the host machine's LLM service.

To Build:
```bash
docker build -t skin-rag-app .
```

To Run:
```bash
docker run -d --name skinapp \
  -p 5001:5000 \
  -e OLLAMA_BASE_URL="http://host.docker.internal:11434" \
  -v "$(pwd)/medical_knowledge_db:/app/medical_knowledge_db" \
  -v "$(pwd)/chroma_db:/app/chroma_db" \
  -v "$(pwd)/uploads:/app/uploads" \
  skin-rag-app
```

---

## 🔹 Technical Implementation Details:
- **Networking**: `host.docker.internal` allows the containerized Flask app to communicate with the Ollama service running on the host OS.
- **Volumes**: Persistent storage is mounted for the `medical_knowledge_db` and `chroma_db` to ensure search indices remain intact during restarts.
- **Environment Variables**: The `OLLAMA_BASE_URL` allows for flexible LLM endpoint configuration without modifying code.

---

## 🔹 Key Technical Highlights for Interviews
- **RAG over Plain LLM**: Prevents medical hallucinations by forcing the model to answer based only on provided medical literature.
- **Edge Privacy**: By using Ollama, the system performs local inference, ensuring sensitive medical data never leaves the local environment.
- **Model Optimization**: The CNN handles spatial feature extraction (texture/edges), while the RAG pipeline handles semantic knowledge retrieval.
- **DevOps Readiness**: Full Dockerization ensures the "it works on my machine" problem is eliminated, providing a clean path to cloud deployment.
