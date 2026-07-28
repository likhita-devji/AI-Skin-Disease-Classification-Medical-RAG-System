"""
Generates all 4 diagrams in the exact visual design style, card layout, headers, 
graphics, and typography of Image 2 (classification_flow.png), customized for Skin Diseases.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_image2_style_diagram_1():
    """System Architecture - MedCare AI Skin Diagnostic RAG (Image 2 Style)"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Main Title
    ax.text(70, 74, "System Architecture - MedCare AI Skin Diagnostic RAG", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Top Flask Oval Badge
    flask_oval = patches.Ellipse((70, 66), 26, 7, ec="#eab308", fc="#fef9c3", lw=1.5)
    ax.add_patch(flask_oval)
    ax.text(70, 66, "Flask\nlocalhost:5000 (Flask)", fontsize=9.5, fontweight='bold', ha='center', color='#854d0e')

    # Card 1: User Interface (Yellow Header)
    card1 = patches.FancyBboxPatch((5, 14), 28, 45, boxstyle="round,pad=0.5,rounding_size=1", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 53.5), 28, 5.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(19, 56, "User Interface", fontsize=12, fontweight='bold', ha='center', color='#1e293b')

    box_ui = patches.FancyBboxPatch((8, 36), 22, 14, boxstyle="round,pad=0.3", ec="#94a3b8", fc="#ffffff", lw=1)
    ax.add_patch(box_ui)
    ax.text(19, 46, "+ MedCare AI >\n/index.html", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    ax.text(19, 28, "• Image Upload / URL\n• User Query\n\nSkin Diagnosis\n+ Treatment Plan", fontsize=9.5, ha='center', color='#334155', fontweight='bold')

    # Uploads folder box below
    box_up = patches.FancyBboxPatch((13, 4), 12, 7, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#3b82f6", lw=1)
    ax.add_patch(box_up)
    ax.text(19, 7.5, "/uploads\nUploads Folder", fontsize=8.5, color='#ffffff', fontweight='bold', ha='center')

    # Card 2: Prediction Server (Flask) (Blue Header)
    card2 = patches.FancyBboxPatch((38, 14), 40, 45, boxstyle="round,pad=0.5", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((38, 53.5), 40, 5.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(58, 56, "Prediction Server (Flask)", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

    box_cnn = patches.FancyBboxPatch((41, 38), 15, 11, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_cnn)
    ax.text(48.5, 43.5, "CNN Model\n(Keras)", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_vs1 = patches.FancyBboxPatch((60, 38), 15, 11, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_vs1)
    ax.text(67.5, 43.5, "Vector Store", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_vs2 = patches.FancyBboxPatch((41, 21), 15, 11, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_vs2)
    ax.text(48.5, 26.5, "Vector Store", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    box_oll = patches.FancyBboxPatch((60, 21), 15, 11, boxstyle="round,pad=0.3", ec="#cbd5e1", fc="#ffffff", lw=1)
    ax.add_patch(box_oll)
    ax.text(67.5, 26.5, "Ollama API", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    # ChromaDB Box at bottom center
    card_chroma = patches.FancyBboxPatch((43, 2), 30, 10, boxstyle="round,pad=0.3", ec="#10b981", fc="#ecfdf5", lw=1.5)
    ax.add_patch(card_chroma)
    ax.text(58, 7, "ChromaDB Embeddings DB\nmedical_knowledge_db (PDFs & MDs)", fontsize=8.5, fontweight='bold', ha='center', color='#065f46')

    # Card 3: Ollama LLM Server (Dark Blue Header)
    card3 = patches.FancyBboxPatch((83, 14), 52, 45, boxstyle="round,pad=0.5", ec="#1e3a8a", fc="#f8fafc", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((83, 53.5), 52, 5.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr3)
    ax.text(109, 56, "Ollama LLM Server", fontsize=12, fontweight='bold', ha='center', color='#ffffff')

    ax.text(109, 45, "localhost:11434 (Ollama)\n\nLlamaMedicine LLM\n\nVector Embedding Model\n+ Grounded Medical Generation", fontsize=9.5, ha='center', color='#334155')

    # Arrows
    ax.annotate('', xy=(38, 43), xytext=(33, 43), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.8))
    ax.annotate('', xy=(83, 43), xytext=(78, 43), arrowprops=dict(arrowstyle="->", color="#1e293b", lw=1.8))

    plt.tight_layout()
    plt.savefig("static/images/system_architecture.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("[Image 1 Recreated in Image 2 Style] static/images/system_architecture.png")

def draw_image2_style_diagram_3():
    """Medical RAG Pipeline Architecture (Image 2 Style)"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')

    # Title
    ax.text(70, 74, "Medical RAG Pipeline Architecture", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Card 1: User Interface (Yellow Header)
    card1 = patches.FancyBboxPatch((5, 18), 30, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#fde047", fc="#fffbeb", lw=1.8)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 59.5), 30, 6.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(20, 62.5, "User Interface", fontsize=13, fontweight='bold', ha='center', color='#1e293b')
    ax.text(20, 45, "+ MedCare AI >\n/index.html\n\n• Image Upload / URL\n• User Query\n\nSkin Diagnosis\n+ Treatment Plan", fontsize=10, ha='center', color='#334155', fontweight='bold')

    # Card 2: Prediction Server (Flask) (Blue Header)
    card2 = patches.FancyBboxPatch((40, 18), 34, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#93c5fd", fc="#eff6ff", lw=1.8)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((40, 59.5), 34, 6.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(57, 62.5, "Prediction Server (Flask)", fontsize=12.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(57, 45, "localhost:5000 (Flask)\n\nCNN Model (Keras) → Retriever\nRetrieves & Combines info", fontsize=10, ha='center', color='#1e3a8a', fontweight='bold')

    # Card 3: Embeddings Database (Green Header)
    card3 = patches.FancyBboxPatch((79, 18), 28, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#a7f3d0", fc="#f0fdf4", lw=1.8)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((79, 59.5), 28, 6.5, boxstyle="round,pad=0.2", ec="#059669", fc="#a7f3d0", lw=0)
    ax.add_patch(hdr3)
    ax.text(93, 62.5, "Embeddings Database", fontsize=12, fontweight='bold', ha='center', color='#065f46')
    ax.text(93, 45, "ChromaDB\n\nmedical_knowledge_db\n✓ Trusted Medical PDFs\n& Treatment Guides", fontsize=10, ha='center', color='#047857', fontweight='bold')

    # Card 4: LLM Generation Server (Dark Blue Header)
    card4 = patches.FancyBboxPatch((111, 18), 25, 48, boxstyle="round,pad=0.5,rounding_size=1.2", ec="#1e3a8a", fc="#f0f9ff", lw=1.8)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((111, 59.5), 25, 6.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(123.5, 62.5, "LLM Generation Server", fontsize=10.5, fontweight='bold', ha='center', color='#ffffff')
    ax.text(123.5, 45, "localhost:11434 (Ollama)\n\nLlamaMedicine LLM\n\n/api/generate", fontsize=10, ha='center', color='#1e3a8a', fontweight='bold')

    # Arrows
    ax.annotate('', xy=(40, 45), xytext=(35, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(79, 45), xytext=(74, 45), arrowprops=dict(arrowstyle="->", color="#eab308", lw=2))
    ax.annotate('', xy=(111, 45), xytext=(107, 45), arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=2))

    ax.plot([20, 20, 123.5, 123.5], [18, 11, 11, 18], color="#1e3a8a", lw=1.5)
    ax.text(70, 4, "Query Tokens + Context Tokens + Output Tokens", fontsize=13, fontweight='bold', ha='center', color='#1e3a8a')

    plt.tight_layout()
    plt.savefig("static/images/architecture_diagram.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("[Image 3 Recreated in Image 2 Style] static/images/architecture_diagram.png")

def draw_image2_style_diagram_4():
    """Skin Diagnostic RAG System Overall Workflow (Image 2 Style)"""
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 70)
    ax.axis('off')

    ax.text(70, 64, "Skin Diagnostic RAG System Workflow", fontsize=18, fontweight='bold', ha='center', color='#1e293b')

    # Step 1: User Input (Yellow Header)
    card1 = patches.FancyBboxPatch((5, 15), 23, 42, boxstyle="round,pad=0.4", ec="#fde047", fc="#fffbeb", lw=1.5)
    ax.add_patch(card1)
    hdr1 = patches.FancyBboxPatch((5, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#eab308", fc="#facc15", lw=0)
    ax.add_patch(hdr1)
    ax.text(16.5, 54, "User Input", fontsize=11, fontweight='bold', ha='center', color='#1e293b')
    ax.text(16.5, 33, "📁 Upload Image\n\n🔗 Image URL", fontsize=9.5, fontweight='bold', ha='center', color='#334155')

    # Step 2: Image Classification (Blue Header)
    card2 = patches.FancyBboxPatch((32, 15), 23, 42, boxstyle="round,pad=0.4", ec="#93c5fd", fc="#eff6ff", lw=1.5)
    ax.add_patch(card2)
    hdr2 = patches.FancyBboxPatch((32, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#2563eb", fc="#3b82f6", lw=0)
    ax.add_patch(hdr2)
    ax.text(43.5, 54, "Image Classification", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(43.5, 33, "CNN Model\n(skin_disease_classifier.keras)\n\nAnalyze Skin Disease", fontsize=9.5, ha='center', color='#1e3a8a', fontweight='bold')

    # Step 3: RAG Pipeline (Orange Header)
    card3 = patches.FancyBboxPatch((59, 15), 23, 42, boxstyle="round,pad=0.4", ec="#fdba74", fc="#fff7ed", lw=1.5)
    ax.add_patch(card3)
    hdr3 = patches.FancyBboxPatch((59, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#ea580c", fc="#f97316", lw=0)
    ax.add_patch(hdr3)
    ax.text(70.5, 54, "RAG Pipeline", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(70.5, 33, "Document Retrieval\n\nContext Chunks\n\nRetrieve QA Chain\nRetrieve & Combine Info", fontsize=9, ha='center', color='#9a3412', fontweight='bold')

    # Step 4: LLM Response Generation (Dark Blue Header)
    card4 = patches.FancyBboxPatch((86, 15), 23, 42, boxstyle="round,pad=0.4", ec="#1e3a8a", fc="#f0f9ff", lw=1.5)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((86, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#1e3a8a", fc="#1e3a8a", lw=0)
    ax.add_patch(hdr4)
    ax.text(97.5, 54, "LLM Generation", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(97.5, 33, "LlamaMedicine LLM\n\nGenerate Response\n\nLocal Ollama Engine", fontsize=9, ha='center', color='#1e3a8a', fontweight='bold')

    # Step 5: Results Display (Light Blue Header)
    card5 = patches.FancyBboxPatch((113, 15), 23, 42, boxstyle="round,pad=0.4", ec="#38bdf8", fc="#f0f9ff", lw=1.5)
    ax.add_patch(card5)
    hdr5 = patches.FancyBboxPatch((113, 51.5), 23, 5.5, boxstyle="round,pad=0.2", ec="#0284c7", fc="#38bdf8", lw=0)
    ax.add_patch(hdr5)
    ax.text(124.5, 54, "Results Display", fontsize=11, fontweight='bold', ha='center', color='#ffffff')
    ax.text(124.5, 33, "🔍 Skin Diagnosis:\n'Melanoma'\n\n☑ Confidence: 92%\n\n📋 Cure & Treatment Steps\n• Surgical Excision\n• Specialist Advice", fontsize=8.5, ha='center', color='#0369a1', fontweight='bold')

    # Connecting Arrows
    ax.annotate('', xy=(32, 36), xytext=(28, 36), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.5))
    ax.annotate('', xy=(59, 36), xytext=(55, 36), arrowprops=dict(arrowstyle="->", color="#3b82f6", lw=1.5))
    ax.annotate('', xy=(86, 36), xytext=(82, 36), arrowprops=dict(arrowstyle="->", color="#f97316", lw=1.5))
    ax.annotate('', xy=(113, 36), xytext=(109, 36), arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=1.5))

    plt.tight_layout()
    plt.savefig("static/images/rag_pipeline.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("[Image 4 Recreated in Image 2 Style] static/images/rag_pipeline.png")

if __name__ == "__main__":
    draw_image2_style_diagram_1()
    draw_image2_style_diagram_3()
    draw_image2_style_diagram_4()
    print("[SUCCESS] All images unified in Image 2 visual design language!")
