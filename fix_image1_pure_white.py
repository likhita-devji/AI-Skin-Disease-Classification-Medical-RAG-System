"""
Fixes system_architecture.png (Image 1) to have a PURE WHITE background matching Image 2 perfectly.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_image1_pure_white():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 90)
    ax.axis('off')

    # Main Title
    ax.text(70, 85, "System Architecture - MedCare AI Skin Diagnostic RAG", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Top Flask Oval
    flask_oval = patches.Ellipse((50, 75), 26, 10, ec="#eab308", fc="#fef9c3", lw=1.8)
    ax.add_patch(flask_oval)
    ax.text(50, 75, "Flask\nlocalhost:5000 (Flask)", fontsize=11, fontweight='bold', ha='center', color='#854d0e')

    # Left Card: User Interface (Yellow Header, Pure White/Pastel body)
    card_ui = patches.FancyBboxPatch((5, 20), 24, 42, boxstyle="round,pad=0.5,rounding_size=1", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card_ui)
    hdr_ui = patches.FancyBboxPatch((5, 56.5), 24, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr_ui)
    ax.text(17, 59, "User Interface", fontsize=11.5, fontweight='bold', ha='center', color='#1e293b')
    ax.text(17, 44, "+ MedCare AI >\n/index.html\n\n• User Query\n\nSkin Diagnosis\n+ Treatment Analysis", fontsize=9.5, ha='center', color='#334155', fontweight='bold')

    # Uploads folder
    fld = patches.FancyBboxPatch((11, 6), 12, 8, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#3b82f6", lw=1)
    ax.add_patch(fld)
    ax.text(17, 10, "/uploads\nUploads Folder", fontsize=8.5, color='#ffffff', fontweight='bold', ha='center')

    # Middle Large Card: Prediction Server (Flask) (Blue Header, Light Blue body)
    card_pred = patches.FancyBboxPatch((35, 15), 44, 47, boxstyle="round,pad=0.5,rounding_size=1", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card_pred)
    hdr_pred = patches.FancyBboxPatch((35, 56.5), 44, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr_pred)
    ax.text(57, 59, "Prediction Server (Flask)", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

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
    ax.text(59, 14, "ChromaDB Embeddings Database", fontsize=10, fontweight='bold', ha='center', color='#065f46')
    ax.text(59, 7, "• medical_knowledge_db\nExpert Medical PDFs & Guides", fontsize=8.5, ha='center', color='#047857', fontweight='bold')

    # Right Top Card: Ollama LLM Server (API)
    card_oll1 = patches.FancyBboxPatch((85, 42), 48, 20, boxstyle="round,pad=0.5", ec="#cbd5e1", fc="#f8fafc", lw=1.5)
    ax.add_patch(card_oll1)
    hdr_oll1 = patches.FancyBboxPatch((85, 56.5), 48, 5.5, boxstyle="round,pad=0.2", ec="#475569", fc="#64748b", lw=0)
    ax.add_patch(hdr_oll1)
    ax.text(109, 59, "Ollama LLM Server", fontsize=11.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(109, 49, "localhost:11434 (Ollama)\nLlamaTokenizer | Vector Embedding Model | LLM API", fontsize=9, ha='center', color='#334155', fontweight='bold')

    # Right Bottom Card: Ollama LLM Server (Model)
    card_oll2 = patches.FancyBboxPatch((85, 12), 48, 24, boxstyle="round,pad=0.5", ec="#cbd5e1", fc="#f8fafc", lw=1.5)
    ax.add_patch(card_oll2)
    hdr_oll2 = patches.FancyBboxPatch((85, 30.5), 48, 5.5, boxstyle="round,pad=0.2", ec="#475569", fc="#64748b", lw=0)
    ax.add_patch(hdr_oll2)
    ax.text(109, 33, "Ollama LLM Server", fontsize=11.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(109, 21, "LlamaMedicine LLM\nPersistent Vector Store | port 5000 | port 5001", fontsize=9.5, ha='center', color='#334155', fontweight='bold')

    # Arrows
    ax.annotate('', xy=(35, 47), xytext=(29, 47), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.8))
    ax.annotate('', xy=(85, 52), xytext=(74, 52), arrowprops=dict(arrowstyle="->", color="#1e293b", lw=1.8))
    ax.annotate('', xy=(85, 24), xytext=(76, 24), arrowprops=dict(arrowstyle="->", color="#1e293b", lw=1.8))

    out_path = "static/images/system_architecture.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[Image 1 Pure White Fix] {out_path}")

if __name__ == "__main__":
    draw_image1_pure_white()
