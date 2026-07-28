"""
Renders all 4 exact architectural & workflow diagrams matching the user's reference screenshots,
customized for Skin Disease Classification & Medical RAG System.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Diagram 1: System Architecture - MedCare AI Skin Diagnostic RAG
def generate_diagram_1():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 90)
    ax.axis('off')

    # Title
    ax.text(70, 85, "System Architecture - MedCare AI Skin Diagnostic RAG", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Top Flask Oval
    flask_oval = patches.Ellipse((50, 75), 26, 10, ec="#eab308", fc="#fef9c3", lw=1.8)
    ax.add_patch(flask_oval)
    ax.text(50, 75, "Flask\nlocalhost:5000 (Flask)", fontsize=11, fontweight='bold', ha='center', color='#854d0e')

    # Left Card: User Interface
    card_ui = patches.FancyBboxPatch((5, 20), 24, 42, boxstyle="round,pad=0.5,rounding_size=1", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card_ui)
    hdr_ui = patches.FancyBboxPatch((5, 56.5), 24, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr_ui)
    ax.text(17, 59, "User Interface", fontsize=11.5, fontweight='bold', ha='center', color='#1e293b')
    ax.text(17, 48, "+ MedCare AI >\n/index.html\n\n• User Query\n\nSkin Diagnosis\n+ Treatment Analysis", fontsize=9.5, ha='center', color='#334155')

    # Uploads folder
    fld = patches.FancyBboxPatch((15, 8), 12, 8, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#3b82f6", lw=1)
    ax.add_patch(fld)
    ax.text(21, 12, "/uploads\nUploads Folder", fontsize=8.5, color='#ffffff', fontweight='bold', ha='center')

    # Middle Large Card: Prediction Server (Flask)
    card_pred = patches.FancyBboxPatch((35, 15), 44, 47, boxstyle="round,pad=0.5,rounding_size=1", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card_pred)
    hdr_pred = patches.FancyBboxPatch((35, 56.5), 44, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr_pred)
    ax.text(57, 59, "Prediction Server (Flask)", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

    # Inside Prediction Server: CNN Model box & Vector Store box
    box_cnn = patches.FancyBboxPatch((38, 42), 16, 10, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_cnn)
    ax.text(46, 47, "CNN Model\n(Keras)", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_vs1 = patches.FancyBboxPatch((58, 42), 16, 10, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_vs1)
    ax.text(66, 47, "Vector Store", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_vs2 = patches.FancyBboxPatch((38, 25), 16, 10, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_vs2)
    ax.text(46, 30, "Vector Store", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_ollama_api = patches.FancyBboxPatch((58, 25), 16, 10, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_ollama_api)
    ax.text(66, 30, "Ollama API", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    # ChromaDB Embeddings DB Card inside bottom
    card_chroma = patches.FancyBboxPatch((42, 2), 34, 18, boxstyle="round,pad=0.4", ec="#a7f3d0", fc="#ecfdf5", lw=1.5)
    ax.add_patch(card_chroma)
    ax.text(59, 15, "ChromaDB Embeddings Database", fontsize=10, fontweight='bold', ha='center', color='#065f46')
    ax.text(59, 8, "• medical_knowledge_db\nExpert Medical PDFs & Guides", fontsize=8.5, ha='center', color='#047857')

    # Right Top Card: Ollama LLM Server (API)
    card_oll1 = patches.FancyBboxPatch((85, 42), 48, 20, boxstyle="round,pad=0.5", ec="#cbd5e1", fc="#f8fafc", lw=1.5)
    ax.add_patch(card_oll1)
    hdr_oll1 = patches.FancyBboxPatch((85, 56.5), 48, 5.5, boxstyle="round,pad=0.2", ec="#475569", fc="#64748b", lw=0)
    ax.add_patch(hdr_oll1)
    ax.text(109, 59, "Ollama LLM Server", fontsize=11.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(109, 49, "localhost:11434 (Ollama)\nLlamaTokenizer | Vector Embedding Model | LLM API", fontsize=9, ha='center', color='#334155')

    # Right Bottom Card: Ollama LLM Server (Model)
    card_oll2 = patches.FancyBboxPatch((85, 12), 48, 24, boxstyle="round,pad=0.5", ec="#cbd5e1", fc="#f8fafc", lw=1.5)
    ax.add_patch(card_oll2)
    hdr_oll2 = patches.FancyBboxPatch((85, 30.5), 48, 5.5, boxstyle="round,pad=0.2", ec="#475569", fc="#64748b", lw=0)
    ax.add_patch(hdr_oll2)
    ax.text(109, 33, "Ollama LLM Server", fontsize=11.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(109, 21, "LlamaMedicine LLM\nPersistent Vector Store | port 5000 | port 5001", fontsize=9.5, ha='center', color='#334155')

    # Arrows
    ax.annotate('', xy=(35, 47), xytext=(29, 47), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.5))
    ax.annotate('', xy=(85, 52), xytext=(74, 52), arrowprops=dict(arrowstyle="->", color="#1e293b", lw=1.5))
    ax.annotate('', xy=(85, 24), xytext=(76, 24), arrowprops=dict(arrowstyle="->", color="#1e293b", lw=1.5))

    out_path = "static/images/system_architecture.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[Generated Diagram 1] {out_path}")

# Diagram 2: CNN-Based Skin Disease Classification Flow
def generate_diagram_2():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Title
    ax.text(70, 74, "CNN-Based Skin Disease Classification Flow", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Card 1: User Input (Yellow)
    card1 = patches.FancyBboxPatch((5, 20), 22, 44, boxstyle="round,pad=0.5", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 58.5), 22, 5.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(16, 61, "User Input", fontsize=11.5, fontweight='bold', ha='center', color='#1e293b')

    btn1 = patches.FancyBboxPatch((7, 48), 18, 7, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(btn1)
    ax.text(16, 51.5, "📷 Upload Patient Image", fontsize=9, fontweight='bold', ha='center', color='#334155')

    btn2 = patches.FancyBboxPatch((7, 38), 18, 7, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(btn2)
    ax.text(16, 41.5, "🔗 Enter Image URL", fontsize=9, fontweight='bold', ha='center', color='#334155')

    box_prev = patches.FancyBboxPatch((7, 23), 18, 12, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_prev)
    ax.text(16, 29, "Preprocess Image", fontsize=9, fontweight='bold', ha='center', color='#64748b')

    # Middle Pipeline: Preprocess & Resized -> Trained CNN Model -> ChromaDB
    ax.annotate('', xy=(34, 40), xytext=(27, 40), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.8))
    ax.text(35, 47, "Preprocess\nImage", fontsize=9, ha='center', color='#475569')

    # Model Cylinder
    cyl = patches.Ellipse((50, 42), 16, 6, ec="#2563eb", fc="#bfdbfe", lw=1.2)
    ax.add_patch(cyl)
    cyl_body = patches.Rectangle((42, 34), 16, 8, ec="#2563eb", fc="#dbeafe", lw=1.2)
    ax.add_patch(cyl_body)
    cyl_base = patches.Ellipse((50, 34), 16, 6, ec="#2563eb", fc="#dbeafe", lw=1.2)
    ax.add_patch(cyl_base)
    ax.text(50, 38, "Trained CNN Model\n(skin_disease_classifier.keras)", fontsize=8.5, fontweight='bold', ha='center', color='#1e3a8a')

    # ChromaDB Box below
    card_db = patches.FancyBboxPatch((40, 16), 20, 12, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#f8fafc", lw=1)
    ax.add_patch(card_db)
    ax.text(50, 24, "ChromaDB\n(medical_knowledge_db)", fontsize=8.5, fontweight='bold', ha='center', color='#1e293b')

    # Card 3: Classification Output List (Blue Header)
    card_out = patches.FancyBboxPatch((68, 18), 32, 46, boxstyle="round,pad=0.5", ec="#60a5fa", fc="#eff6ff", lw=1.8)
    ax.add_patch(card_out)
    hdr_out = patches.FancyBboxPatch((68, 58.5), 32, 5.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr_out)
    ax.text(84, 61, "Classification Output", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

    classes = [
        "☑ Actinic Keratoses (akiec)",
        "☑ Basal Cell Carcinoma (bcc)",
        "☑ Benign Keratosis (bkl)",
        "☑ Dermatofibroma (df)",
        "☑ Melanoma (mel)",
        "☑ Melanocytic Nevi (nv)",
        "☑ Vascular Lesions (vasc)"
    ]
    for idx, cname in enumerate(classes):
        ax.text(71, 52 - (idx * 4.8), cname, fontsize=9, fontweight='bold', color='#1e3a8a')

    # Card 4: Examples Column (Far Right Blue Header)
    card_ex = patches.FancyBboxPatch((106, 18), 28, 46, boxstyle="round,pad=0.5", ec="#2563eb", fc="#ffffff", lw=1.8)
    ax.add_patch(card_ex)
    hdr_ex = patches.FancyBboxPatch((106, 58.5), 28, 5.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1d4ed8", lw=0)
    ax.add_patch(hdr_ex)
    ax.text(120, 61, "Examples", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

    ex_labels = ["Melanoma", "Basal Cell", "Benign Keratosis", "Actinic Keratosis"]
    for idx, elab in enumerate(ex_labels):
        box_thumb = patches.FancyBboxPatch((110, 48 - (idx * 9.5)), 20, 6.5, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#f1f5f9", lw=0.8)
        ax.add_patch(box_thumb)
        ax.text(120, 51.5 - (idx * 9.5), f"📌 {elab}", fontsize=8.5, fontweight='bold', ha='center', color='#334155')

    ax.annotate('', xy=(68, 40), xytext=(58, 40), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.8))

    out_path = "static/images/classification_flow.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[Generated Diagram 2] {out_path}")

# Diagram 3: Medical RAG Pipeline Architecture (Pastel White background 4-column)
def generate_diagram_3():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    ax.text(70, 74, "Medical RAG Pipeline Architecture", fontsize=20, fontweight='bold', ha='center', color='#1e293b')

    # Card 1 (Yellow)
    card1 = patches.FancyBboxPatch((5, 18), 30, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 59.5), 30, 6.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(20, 62.5, "User Interface", fontsize=13, fontweight='bold', ha='center', color='#1e293b')
    ax.text(20, 45, "+ MedCare AI >\n/index.html\n\n• Image Upload / URL\n• User Query\n\nSkin Diagnosis\n+ Treatment Plan", fontsize=10, ha='center', color='#334155')

    # Card 2 (Blue)
    card2 = patches.FancyBboxPatch((40, 18), 34, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((40, 59.5), 34, 6.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(57, 62.5, "Prediction Server (Flask)", fontsize=12.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(57, 45, "localhost:5000 (Flask)\n\nCNN Model (Keras) → Retriever\nRetrieves & Combines info", fontsize=10, ha='center', color='#1e3a8a')

    # Card 3 (Green)
    card3 = patches.FancyBboxPatch((79, 18), 28, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#a7f3d0", fc="#f0fdf4", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((79, 59.5), 28, 6.5, boxstyle="round,pad=0.2", ec="#059669", fc="#a7f3d0", lw=0)
    ax.add_patch(hdr3)
    ax.text(93, 62.5, "Embeddings Database", fontsize=12, fontweight='bold', ha='center', color='#065f46')
    ax.text(93, 45, "ChromaDB\n\nmedical_knowledge_db\n✓ Trusted Medical PDFs\n& Treatment Guides", fontsize=10, ha='center', color='#047857')

    # Card 4 (Navy)
    card4 = patches.FancyBboxPatch((111, 18), 25, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#1e3a8a", fc="#f0f9ff", lw=1.8)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((111, 59.5), 25, 6.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(123.5, 62.5, "LLM Generation Server", fontsize=10.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(123.5, 45, "localhost:11434 (Ollama)\n\nLlamaMedicine LLM\n\n/api/generate", fontsize=10, ha='center', color='#1e3a8a')

    # Arrows
    ax.annotate('', xy=(40, 45), xytext=(35, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(79, 45), xytext=(74, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(111, 45), xytext=(107, 45), arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=2))

    ax.plot([20, 20, 123.5, 123.5], [18, 11, 11, 18], color="#1e3a8a", lw=1.5)
    ax.text(70, 4, "Query Tokens + Context Tokens + Output Tokens", fontsize=13, fontweight='bold', ha='center', color='#1e3a8a')

    out_path = "static/images/architecture_diagram.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[Generated Diagram 3] {out_path}")

# Diagram 4: Skin Diagnostic RAG System (Overall Project Workflow 5-step)
def generate_diagram_4():
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 70)
    ax.axis('off')

    # Title
    ax.text(70, 64, "Skin Diagnostic RAG System", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Step 1: User Input (Yellow)
    card1 = patches.FancyBboxPatch((5, 15), 23, 42, boxstyle="round,pad=0.4", ec="#fde047", fc="#fffbeb", lw=1.5)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(16.5, 54, "User Input", fontsize=11, fontweight='bold', ha='center', color='#1e293b')
    ax.text(16.5, 33, "📁 Upload Image\n\n🔗 Image URL", fontsize=9.5, fontweight='bold', ha='center', color='#334155')

    # Step 2: Image Classification (Blue)
    card2 = patches.FancyBboxPatch((32, 15), 23, 42, boxstyle="round,pad=0.4", ec="#93c5fd", fc="#eff6ff", lw=1.5)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((32, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(43.5, 54, "Image Classification", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(43.5, 33, "CNN Model\n(skin_disease_classifier.keras)\n\nAnalyze Disease Type", fontsize=9.5, ha='center', color='#1e3a8a')

    # Step 3: RAG Pipeline (Orange)
    card3 = patches.FancyBboxPatch((59, 15), 23, 42, boxstyle="round,pad=0.4", ec="#fdba74", fc="#fff7ed", lw=1.5)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((59, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#ea580c", fc="#f97316", lw=0)
    ax.add_patch(hdr3)
    ax.text(70.5, 54, "RAG Pipeline", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(70.5, 33, "Document Retrieval\n\nContext Chunks\n\nRetrieve QA Chain\nRetrieve & Combine Info", fontsize=9, ha='center', color='#9a3412')

    # Step 4: LLM Response Generation (Dark Navy)
    card4 = patches.FancyBboxPatch((86, 15), 23, 42, boxstyle="round,pad=0.4", ec="#1e3a8a", fc="#f0f9ff", lw=1.5)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((86, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(97.5, 54, "LLM Generation", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(97.5, 33, "LlamaMedicine LLM\n\nGenerate Response\n\nLocal Ollama Engine", fontsize=9, ha='center', color='#1e3a8a')

    # Step 5: Results Display (Light Blue)
    card5 = patches.FancyBboxPatch((113, 15), 23, 42, boxstyle="round,pad=0.4", ec="#38bdf8", fc="#f0f9ff", lw=1.5)
    ax.add_patch(card5)
    hdr5 = patches.FancyBboxPatch((113, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#0284c7", fc="#38bdf8", lw=0)
    ax.add_patch(hdr5)
    ax.text(124.5, 54, "Results Display", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(124.5, 33, "🔍 Skin Diagnosis:\n'Melanoma'\n\n☑ Confidence: 92%\n\n📋 Cure & Treatment Steps\n• Surgical Excision\n• Specialist Advice", fontsize=8.5, ha='center', color='#0369a1')

    # Connecting Arrows between 5 steps
    ax.annotate('', xy=(32, 36), xytext=(28, 36), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.5))
    ax.annotate('', xy=(59, 36), xytext=(55, 36), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.5))
    ax.annotate('', xy=(86, 36), xytext=(82, 36), arrowprops=dict(arrowstyle="->", color="#f97316", lw=1.5))
    ax.annotate('', xy=(113, 36), xytext=(109, 36), arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=1.5))

    out_path = "static/images/rag_pipeline.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[Generated Diagram 4] {out_path}")

if __name__ == "__main__":
    generate_diagram_1()
    generate_diagram_2()
    generate_diagram_3()
    generate_diagram_4()
    print("[SUCCESS] All 4 reference diagrams regenerated with exact matching structure!")
