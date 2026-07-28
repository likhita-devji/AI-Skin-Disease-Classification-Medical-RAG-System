import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_cnn_classification_diagram():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=200)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')

    # Title
    ax.text(50, 46, "CNN-Based Skin Disease Classification Flow", fontsize=16, fontweight='bold', ha='center', color='#1e293b')

    # Card 1: Input Image (Yellow)
    rect1 = patches.FancyBboxPatch((4, 10), 20, 30, boxstyle="round,pad=0.3", ec="#eab308", fc="#fef9c3", lw=1.5)
    ax.add_patch(rect1)
    ax.text(14, 37, "Input Image", fontsize=11, fontweight='bold', ha='center', color='#854d0e')
    ax.text(14, 28, "• Skin Lesion Photo\n• RGB Array Preprocessing\n• Resized to 224x224", fontsize=9, ha='center', color='#475569')

    # Arrow 1 -> 2
    ax.annotate('', xy=(28, 25), xytext=(24, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 2: CNN Model (Blue)
    rect2 = patches.FancyBboxPatch((28, 10), 22, 30, boxstyle="round,pad=0.3", ec="#3b82f6", fc="#eff6ff", lw=1.5)
    ax.add_patch(rect2)
    ax.text(39, 37, "EfficientNet CNN", fontsize=11, fontweight='bold', ha='center', color='#1e40af')
    ax.text(39, 28, "• Feature Extractor\n• Batch Normalization\n• Dropout (0.3 / 0.2)\n• Dense Softmax Layer", fontsize=9, ha='center', color='#475569')

    # Arrow 2 -> 3
    ax.annotate('', xy=(54, 25), xytext=(50, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 3: Probability Map (Green)
    rect3 = patches.FancyBboxPatch((54, 10), 22, 30, boxstyle="round,pad=0.3", ec="#10b981", fc="#ecfdf5", lw=1.5)
    ax.add_patch(rect3)
    ax.text(65, 37, "Probability Scores", fontsize=11, fontweight='bold', ha='center', color='#065f46')
    ax.text(65, 27, "• Melanoma (mel)\n• Basal Cell (bcc)\n• Benign Kerat. (bkl)\n• Nevi Moles (nv)\n• Actinic / Vasc / DF", fontsize=9, ha='center', color='#475569')

    # Arrow 3 -> 4
    ax.annotate('', xy=(80, 25), xytext=(76, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 4: Prediction & Risk (Purple)
    rect4 = patches.FancyBboxPatch((80, 10), 16, 30, boxstyle="round,pad=0.3", ec="#8b5cf6", fc="#f5f3ff", lw=1.5)
    ax.add_patch(rect4)
    ax.text(88, 37, "Classification", fontsize=11, fontweight='bold', ha='center', color='#5b21b6')
    ax.text(88, 27, "• Top-1 Prediction\n• Risk Badge\n• Top-3 Distribution", fontsize=9, ha='center', color='#475569')

    out_path = "static/images/system_architecture.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_path}")

def generate_rag_workflow_diagram():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=200)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')

    # Title
    ax.text(50, 46, "Overall Project Workflow & RAG Pipeline", fontsize=16, fontweight='bold', ha='center', color='#1e293b')

    # Card 1: User Question (Yellow)
    rect1 = patches.FancyBboxPatch((4, 10), 20, 30, boxstyle="round,pad=0.3", ec="#eab308", fc="#fef9c3", lw=1.5)
    ax.add_patch(rect1)
    ax.text(14, 37, "User Question", fontsize=11, fontweight='bold', ha='center', color='#854d0e')
    ax.text(14, 28, "• Disease Prediction\n• Medical Query\n• Clinical Request", fontsize=9, ha='center', color='#475569')

    # Arrow 1 -> 2
    ax.annotate('', xy=(28, 25), xytext=(24, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 2: Sentence Embeddings (Blue)
    rect2 = patches.FancyBboxPatch((28, 10), 22, 30, boxstyle="round,pad=0.3", ec="#3b82f6", fc="#eff6ff", lw=1.5)
    ax.add_patch(rect2)
    ax.text(39, 37, "Dense Embeddings", fontsize=11, fontweight='bold', ha='center', color='#1e40af')
    ax.text(39, 28, "• SentenceTransformer\n• all-MiniLM-L6-v2\n• Vector Encoding", fontsize=9, ha='center', color='#475569')

    # Arrow 2 -> 3
    ax.annotate('', xy=(54, 25), xytext=(50, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 3: ChromaDB Search (Green)
    rect3 = patches.FancyBboxPatch((54, 10), 22, 30, boxstyle="round,pad=0.3", ec="#10b981", fc="#ecfdf5", lw=1.5)
    ax.add_patch(rect3)
    ax.text(65, 37, "ChromaDB Search", fontsize=11, fontweight='bold', ha='center', color='#065f46')
    ax.text(65, 27, "• Medical PDFs & MDs\n• Cosine Similarity\n• Context Retrieval", fontsize=9, ha='center', color='#475569')

    # Arrow 3 -> 4
    ax.annotate('', xy=(80, 25), xytext=(76, 25), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2))

    # Card 4: Grounded Response (Navy)
    rect4 = patches.FancyBboxPatch((80, 10), 16, 30, boxstyle="round,pad=0.3", ec="#1e3a8a", fc="#f0f9ff", lw=1.5)
    ax.add_patch(rect4)
    ax.text(88, 37, "Grounded Output", fontsize=11, fontweight='bold', ha='center', color='#1e3a8a')
    ax.text(88, 27, "• Local Ollama LLM\n• Zero Hallucination\n• Cure & Treatments", fontsize=9, ha='center', color='#475569')

    out_path = "static/images/rag_pipeline.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate_cnn_classification_diagram()
    generate_rag_workflow_diagram()
