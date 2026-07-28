"""
Recreates all 3 diagrams in the exact same visual style, typography, pastel card colors, 
top title strips, sub-box cards, and rounded corner styling as Image 1.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_diagram_1_architecture():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Main Title
    ax.text(70, 74, "Medical RAG Pipeline Architecture", fontsize=20, fontweight='bold', ha='center', color='#1e293b')

    # Column 1: User Interface (Yellow)
    card1 = patches.FancyBboxPatch((5, 18), 30, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 59.5), 30, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(20, 62.5, "User Interface", fontsize=13, fontweight='bold', ha='center', color='#1e293b')

    win1 = patches.FancyBboxPatch((7.5, 43), 25, 13, boxstyle="round,pad=0.3,rounding_size=0.6", ec="#94a3b8", fc="#ffffff", lw=1.2)
    ax.add_patch(win1)
    ax.text(9.5, 53.5, "• • •", fontsize=10, color='#94a3b8')
    ax.text(11, 49.5, "+ DermCare AI >", fontsize=10, fontweight='bold', color='#1e293b')
    rect_url = patches.Rectangle((9, 44.5), 22, 3.5, ec="#cbd5e1", fc="#f8fafc", lw=0.8)
    ax.add_patch(rect_url)
    ax.text(10, 45.5, "/index.html", fontsize=9, color='#475569')

    ax.text(8.5, 38, "• Image Upload / URL", fontsize=10, color='#d97706', fontweight='bold')
    ax.text(8.5, 33, "• User Query", fontsize=10, color='#d97706', fontweight='bold')
    ax.text(8.5, 25, "• Skin Diagnosis\n  + Treatment Plan", fontsize=10.5, color='#334155', fontweight='bold')

    # Column 2: Prediction Server (Flask) (Blue)
    card2 = patches.FancyBboxPatch((40, 18), 34, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((40, 59.5), 34, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(57, 62.5, "Prediction Server (Flask)", fontsize=12.5, fontweight='bold', ha='center', color='#ffffff')

    ax.text(57, 54, "localhost:5000 (Flask)", fontsize=11, color='#1e3a8a', ha='center')

    box_keras = patches.FancyBboxPatch((43, 40), 10, 9, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_keras)
    ax.text(48, 44.5, "Keras\nModel", fontsize=9, fontweight='bold', ha='center', color='#1e293b')

    cyl = patches.Ellipse((65, 46), 10, 4, ec="#2563eb", fc="#bfdbfe", lw=1.2)
    ax.add_patch(cyl)
    cyl_body = patches.Rectangle((60, 40), 10, 6, ec="#2563eb", fc="#dbeafe", lw=1.2)
    ax.add_patch(cyl_body)
    cyl_base = patches.Ellipse((65, 40), 10, 4, ec="#2563eb", fc="#dbeafe", lw=1.2)
    ax.add_patch(cyl_base)

    box_cnn = patches.FancyBboxPatch((43, 26), 10, 8, boxstyle="round,pad=0.2", ec="#2563eb", fc="#ffffff", lw=1)
    ax.add_patch(box_cnn)
    ax.text(48, 30, "CNN", fontsize=10, fontweight='bold', ha='center', color='#1d4ed8')

    ax.text(65, 29, "Retriever", fontsize=11, fontweight='bold', ha='center', color='#1e293b')
    ax.text(65, 22, "Retrieves & combines info", fontsize=9, ha='center', color='#475569')

    ax.annotate('', xy=(59, 44.5), xytext=(53, 44.5), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.5))
    ax.annotate('', xy=(59, 30), xytext=(53, 30), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.5))

    # Column 3: Embeddings Database (Green)
    card3 = patches.FancyBboxPatch((79, 18), 28, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#a7f3d0", fc="#f0fdf4", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((79, 59.5), 28, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#059669", fc="#a7f3d0", lw=0)
    ax.add_patch(hdr3)
    ax.text(93, 62.5, "Embeddings Database", fontsize=12, fontweight='bold', ha='center', color='#065f46')

    ax.text(93, 53.5, "ChromaDB", fontsize=11, fontweight='bold', color='#047857', ha='center')

    for offset in [84, 89, 94]:
        doc_rect = patches.Rectangle((offset, 43), 6, 8, ec="#94a3b8", fc="#ffffff", lw=1)
        ax.add_patch(doc_rect)
        ax.text(offset+3, 47, "PDF", fontsize=7, fontweight='bold', ha='center', color='#dc2626')

    kbox = patches.FancyBboxPatch((82, 24), 22, 14, boxstyle="round,pad=0.3,rounding_size=0.6", ec="#059669", fc="#d1fae5", lw=1.2)
    ax.add_patch(kbox)
    ax.text(93, 33, "medical_knowledge_db", fontsize=9.5, fontweight='bold', ha='center', color='#065f46')
    ax.text(93, 27, "✓ Trusted medical PDFs\n  & Cure Guides", fontsize=9, ha='center', color='#047857')

    # Column 4: LLM Generation Server (Dark Navy)
    card4 = patches.FancyBboxPatch((111, 18), 25, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#1e3a8a", fc="#f0f9ff", lw=1.8)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((111, 59.5), 25, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(123.5, 62.5, "LLM Generation Server", fontsize=10.5, fontweight='bold', ha='center', color='#ffffff')

    ax.text(123.5, 54, "localhost:11434 (Ollama)", fontsize=9.5, color='#1e3a8a', ha='center')

    box_llama = patches.FancyBboxPatch((114, 34), 19, 16, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_llama)
    ax.text(123.5, 42, "Llama LLM", fontsize=11, fontweight='bold', ha='center', color='#1e3a8a')
    ax.text(123.5, 36, "Local Inference", fontsize=9, ha='center', color='#475569')

    box_api = patches.Rectangle((114, 24), 19, 5, ec="#cbd5e1", fc="#ffffff", lw=0.8)
    ax.add_patch(box_api)
    ax.text(123.5, 26.2, "/api/generate", fontsize=9, color='#475569', ha='center')

    # Connections
    ax.annotate('', xy=(40, 45), xytext=(35, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.text(37.5, 47, "HTTP\nRequest", fontsize=8.5, fontweight='bold', ha='center', color='#ca8a04')
    ax.annotate('', xy=(79, 45), xytext=(74, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(111, 45), xytext=(107, 45), arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=2))

    ax.plot([20, 20, 123.5, 123.5], [18, 11, 11, 18], color="#1e3a8a", lw=1.5)
    tok_box = patches.FancyBboxPatch((60, 9), 20, 4, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=0.8)
    ax.add_patch(tok_box)
    ax.text(70, 10.8, "Token Usage", fontsize=8.5, color='#475569', ha='center')

    ax.text(70, 4, "Query Tokens + Context Tokens + Output Tokens", fontsize=13, fontweight='bold', ha='center', color='#1e3a8a')

    plt.tight_layout()
    plt.savefig("static/images/architecture_diagram.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()

def draw_diagram_2_cnn_flow():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Main Title
    ax.text(70, 74, "CNN-Based Skin Disease Classification Flow", fontsize=20, fontweight='bold', ha='center', color='#1e293b')

    # Column 1: Input Preprocessing (Yellow)
    card1 = patches.FancyBboxPatch((5, 18), 30, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 59.5), 30, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(20, 62.5, "Input Preprocessing", fontsize=13, fontweight='bold', ha='center', color='#1e293b')

    box_img = patches.FancyBboxPatch((8, 38), 24, 18, boxstyle="round,pad=0.3", ec="#94a3b8", fc="#ffffff", lw=1.2)
    ax.add_patch(box_img)
    ax.text(20, 49, "Skin Lesion Photo", fontsize=11, fontweight='bold', ha='center', color='#1e293b')
    ax.text(20, 42, "RGB Dermatoscopy Image", fontsize=9, ha='center', color='#64748b')

    ax.text(8.5, 30, "• Tensor Resizing (224x224)", fontsize=9.5, color='#d97706', fontweight='bold')
    ax.text(8.5, 24, "• Color Normalization", fontsize=9.5, color='#d97706', fontweight='bold')

    # Column 2: EfficientNet CNN Model (Blue)
    card2 = patches.FancyBboxPatch((40, 18), 34, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((40, 59.5), 34, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(57, 62.5, "EfficientNetB0 Backbone", fontsize=12.5, fontweight='bold', ha='center', color='#ffffff')

    box_conv = patches.FancyBboxPatch((43, 38), 28, 18, boxstyle="round,pad=0.3", ec="#2563eb", fc="#ffffff", lw=1)
    ax.add_patch(box_conv)
    ax.text(57, 50, "Feature Extractor", fontsize=11, fontweight='bold', ha='center', color='#1d4ed8')
    ax.text(57, 42, "MBConv Blocks & Spatial Filters\nGlobal Average Pooling", fontsize=9, ha='center', color='#475569')

    box_dense = patches.FancyBboxPatch((43, 22), 28, 12, boxstyle="round,pad=0.3", ec="#2563eb", fc="#dbeafe", lw=1)
    ax.add_patch(box_dense)
    ax.text(57, 30, "Classification Head", fontsize=10.5, fontweight='bold', ha='center', color='#1e3a8a')
    ax.text(57, 25, "Dense Layer (256) + Softmax (7)", fontsize=9, ha='center', color='#1e40af')

    # Column 3: Softmax Probabilities (Green)
    card3 = patches.FancyBboxPatch((79, 18), 28, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#a7f3d0", fc="#f0fdf4", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((79, 59.5), 28, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#059669", fc="#a7f3d0", lw=0)
    ax.add_patch(hdr3)
    ax.text(93, 62.5, "Probability Scores", fontsize=12, fontweight='bold', ha='center', color='#065f46')

    box_prob = patches.FancyBboxPatch((82, 24), 22, 30, boxstyle="round,pad=0.3", ec="#059669", fc="#ffffff", lw=1)
    ax.add_patch(box_prob)
    ax.text(93, 49, "7 Disease Classes", fontsize=10, fontweight='bold', ha='center', color='#065f46')
    ax.text(93, 43, "• Melanoma (mel)\n• Basal Cell (bcc)\n• Benign Kerat. (bkl)\n• Nevi Moles (nv)\n• Actinic (akiec)\n• Vascular (vasc)\n• Dermatofibroma (df)", fontsize=9, ha='center', color='#334155')

    # Column 4: Diagnostic Output (Purple)
    card4 = patches.FancyBboxPatch((111, 18), 25, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#c084fc", fc="#faf5ff", lw=1.8)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((111, 59.5), 25, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#9333ea", fc="#a855f7", lw=0)
    ax.add_patch(hdr4)
    ax.text(123.5, 62.5, "Diagnostic Result", fontsize=11, fontweight='bold', ha='center', color='#ffffff')

    box_res = patches.FancyBboxPatch((114, 32), 19, 22, boxstyle="round,pad=0.3", ec="#9333ea", fc="#ffffff", lw=1)
    ax.add_patch(box_res)
    ax.text(123.5, 48, "Predicted Disease", fontsize=10, fontweight='bold', ha='center', color='#6b21a8')
    ax.text(123.5, 42, "+ Confidence %", fontsize=9.5, fontweight='bold', ha='center', color='#9333ea')
    ax.text(123.5, 36, "+ Severity Badge", fontsize=9, ha='center', color='#475569')

    # Arrows
    ax.annotate('', xy=(40, 45), xytext=(35, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(79, 45), xytext=(74, 45), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2))
    ax.annotate('', xy=(111, 45), xytext=(107, 45), arrowprops=dict(arrowstyle="->", color="#9333ea", lw=2))

    ax.plot([20, 20, 123.5, 123.5], [18, 11, 11, 18], color="#2563eb", lw=1.5)
    ax.text(70, 4, "Spatial Feature Extraction + Deep CNN Classification Pipeline", fontsize=13, fontweight='bold', ha='center', color='#1e3a8a')

    plt.tight_layout()
    plt.savefig("static/images/system_architecture.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()

def draw_diagram_3_rag_workflow():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Main Title
    ax.text(70, 74, "Overall Project Workflow & RAG Pipeline", fontsize=20, fontweight='bold', ha='center', color='#1e293b')

    # Column 1: User Query & Condition (Yellow)
    card1 = patches.FancyBboxPatch((5, 18), 30, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 59.5), 30, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(20, 62.5, "User Input & Prediction", fontsize=12, fontweight='bold', ha='center', color='#1e293b')

    box_q = patches.FancyBboxPatch((8, 36), 24, 20, boxstyle="round,pad=0.3", ec="#eab308", fc="#ffffff", lw=1)
    ax.add_patch(box_q)
    ax.text(20, 50, "Input Query", fontsize=11, fontweight='bold', ha='center', color='#854d0e')
    ax.text(20, 42, "• User Question\n• Disease Code\n• Clinical Context", fontsize=9, ha='center', color='#475569')

    # Column 2: Vector Embedding (Blue)
    card2 = patches.FancyBboxPatch((40, 18), 34, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((40, 59.5), 34, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(57, 62.5, "Dense Vector Embedding", fontsize=12.5, fontweight='bold', ha='center', color='#ffffff')

    box_emb = patches.FancyBboxPatch((43, 36), 28, 20, boxstyle="round,pad=0.3", ec="#2563eb", fc="#ffffff", lw=1)
    ax.add_patch(box_emb)
    ax.text(57, 50, "SentenceTransformer", fontsize=11, fontweight='bold', ha='center', color='#1d4ed8')
    ax.text(57, 42, "all-MiniLM-L6-v2\n384-dimensional Vector", fontsize=9, ha='center', color='#475569')

    # Column 3: ChromaDB Vector Retrieval (Green)
    card3 = patches.FancyBboxPatch((79, 18), 28, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#a7f3d0", fc="#f0fdf4", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((79, 59.5), 28, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#059669", fc="#a7f3d0", lw=0)
    ax.add_patch(hdr3)
    ax.text(93, 62.5, "ChromaDB Retrieval", fontsize=12, fontweight='bold', ha='center', color='#065f46')

    box_db = patches.FancyBboxPatch((82, 36), 22, 20, boxstyle="round,pad=0.3", ec="#059669", fc="#ffffff", lw=1)
    ax.add_patch(box_db)
    ax.text(93, 50, "Cosine Search", fontsize=11, fontweight='bold', ha='center', color='#065f46')
    ax.text(93, 42, "Top-3 Medical Chunks\nPDF & MD Literature", fontsize=9, ha='center', color='#475569')

    # Column 4: Grounded Answer & Cure Plan (Navy)
    card4 = patches.FancyBboxPatch((111, 18), 25, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#1e3a8a", fc="#f0f9ff", lw=1.8)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((111, 59.5), 25, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(123.5, 62.5, "Grounded Output", fontsize=11, fontweight='bold', ha='center', color='#ffffff')

    box_out = patches.FancyBboxPatch((114, 36), 19, 20, boxstyle="round,pad=0.3", ec="#1e3a8a", fc="#ffffff", lw=1)
    ax.add_patch(box_out)
    ax.text(123.5, 50, "Grounded Answer", fontsize=10.5, fontweight='bold', ha='center', color='#1e3a8a')
    ax.text(123.5, 42, "• Cure & Treatments\n• Surgical Options\n• Zero Hallucination", fontsize=9, ha='center', color='#475569')

    # Arrows
    ax.annotate('', xy=(40, 45), xytext=(35, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(79, 45), xytext=(74, 45), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2))
    ax.annotate('', xy=(111, 45), xytext=(107, 45), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))

    ax.plot([20, 20, 123.5, 123.5], [18, 11, 11, 18], color="#059669", lw=1.5)
    ax.text(70, 4, "Dense Vector Embeddings + Grounded Medical Knowledge RAG Flow", fontsize=13, fontweight='bold', ha='center', color='#065f46')

    plt.tight_layout()
    plt.savefig("static/images/rag_pipeline.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()

if __name__ == "__main__":
    draw_diagram_1_architecture()
    draw_diagram_2_cnn_flow()
    draw_diagram_3_rag_workflow()
    print("[Success] All 3 diagrams updated with 100% identical pastel card styling!")
