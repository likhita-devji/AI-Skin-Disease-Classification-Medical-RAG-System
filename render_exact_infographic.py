"""
Renders a 1:1 high-resolution vector infographic matching the user's exact uploaded image:
'AI SKIN DISEASE CLASSIFICATION MEDICAL RAG SYSTEM - SYSTEM ARCHITECTURE'
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_exact_infographic():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # =========================================================================
    # 1. Header Section
    # =========================================================================
    ax.text(80, 94, "AI SKIN DISEASE CLASSIFICATION MEDICAL RAG SYSTEM", 
            fontsize=20, fontweight='extra bold', ha='center', color='#0f172a')
    
    # Subtitle line
    ax.plot([45, 115], [88, 88], color='#8b5cf6', lw=1.5)
    ax.scatter([45, 115], [88, 88], color='#8b5cf6', s=25, zorder=5)
    ax.text(80, 88, " SYSTEM ARCHITECTURE ", fontsize=13, fontweight='bold', ha='center', color='#7c3aed', backgroundcolor='#ffffff')

    ax.text(80, 82, "An end-to-end AI system that classifies skin diseases from images and provides\nevidence-based medical explanations using a Medical RAG pipeline.", 
            fontsize=10, ha='center', color='#475569')

    # =========================================================================
    # 2. Four Main Column Cards
    # =========================================================================
    
    # Card 1: 1. USER INTERFACE (Green)
    c1_bg = patches.FancyBboxPatch((6, 32), 33, 44, boxstyle="round,pad=0.5,rounding_size=1", ec="#86efac", fc="#f0fdf4", lw=1.5)
    ax.add_patch(c1_bg)
    c1_hdr = patches.FancyBboxPatch((6, 70.5), 33, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#16a34a", fc="#16a34a", lw=0)
    ax.add_patch(c1_hdr)
    ax.text(22.5, 73, "1. USER INTERFACE", fontsize=11, fontweight='bold', ha='center', color='#ffffff')

    # Items inside Card 1
    items1 = [
        ("🖥️", "Web Application\nDashboard"),
        ("☁️", "Upload Skin Image\n(JPG, PNG, JPEG)"),
        ("💬", "Ask Question\n(Symptoms, Treatment, Prevention)"),
        ("📋", "View Report\n& Recommendations")
    ]
    for idx, (icon, label) in enumerate(items1):
        y_pos = 62 - (idx * 9)
        ibox = patches.FancyBboxPatch((8, y_pos), 29, 7.5, boxstyle="round,pad=0.2", ec="#bbf7d0", fc="#ffffff", lw=1)
        ax.add_patch(ibox)
        ax.text(11, y_pos + 3.8, icon, fontsize=12, ha='center', va='center')
        ax.text(15, y_pos + 3.8, label, fontsize=8.5, fontweight='bold', color='#1e293b', va='center')

    # Card 2: 2. PREDICTION SERVER (Blue)
    c2_bg = patches.FancyBboxPatch((44, 32), 33, 44, boxstyle="round,pad=0.5,rounding_size=1", ec="#93c5fd", fc="#eff6ff", lw=1.5)
    ax.add_patch(c2_bg)
    c2_hdr = patches.FancyBboxPatch((44, 70.5), 33, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#2563eb", fc="#2563eb", lw=0)
    ax.add_patch(c2_hdr)
    ax.text(60.5, 73, "2. PREDICTION SERVER", fontsize=11, fontweight='bold', ha='center', color='#ffffff')

    # Brain Circuit Graphic
    ax.text(60.5, 58, "🧠", fontsize=34, ha='center')
    ax.text(60.5, 48, "CNN MODEL\n(Image Classification)", fontsize=10, fontweight='bold', ha='center', color='#1e3a8a')
    
    # Dashed line inside Card 2
    ax.plot([48, 73], [44, 44], color='#93c5fd', lw=1, linestyle='--')

    ax.text(60.5, 39, "📊", fontsize=16, ha='center')
    ax.text(60.5, 35, "Disease Prediction\n& Confidence Score", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')

    # Card 3: 3. MEDICAL RAG SYSTEM (Orange)
    c3_bg = patches.FancyBboxPatch((82, 32), 33, 44, boxstyle="round,pad=0.5,rounding_size=1", ec="#fed7aa", fc="#fff7ed", lw=1.5)
    ax.add_patch(c3_bg)
    c3_hdr = patches.FancyBboxPatch((82, 70.5), 33, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#ea580c", fc="#ea580c", lw=0)
    ax.add_patch(c3_hdr)
    ax.text(98.5, 73, "3. MEDICAL RAG SYSTEM", fontsize=11, fontweight='bold', ha='center', color='#ffffff')

    items3 = [
        ("📁", "Document Loader", "(Medical PDFs, Guidelines)"),
        ("✂️", "Text Splitter", "(Chunking Documents)"),
        ("[*]", "Embeddings", "(Text to Vector)"),
        ("🛢️", "Vector Database", "(ChromaDB)"),
        ("🔍", "Retriever", "(Semantic Search)")
    ]
    for idx, (icon, title, sub) in enumerate(items3):
        y_pos = 64 - (idx * 7)
        ax.text(86, y_pos, icon, fontsize=10, ha='center', color='#ea580c')
        ax.text(90, y_pos, title, fontsize=8.5, fontweight='bold', color='#1e293b')
        ax.text(103, y_pos, sub, fontsize=7.5, color='#64748b')
        if idx < 4:
            ax.plot([85, 112], [y_pos - 2.5, y_pos - 2.5], color='#ffedd5', lw=1, linestyle='--')

    # Card 4: 4. LLM RESPONSE GENERATION (Purple)
    c4_bg = patches.FancyBboxPatch((120, 32), 34, 44, boxstyle="round,pad=0.5,rounding_size=1", ec="#ddd6fe", fc="#faf5ff", lw=1.5)
    ax.add_patch(c4_bg)
    c4_hdr = patches.FancyBboxPatch((120, 70.5), 34, 5.5, boxstyle="round,pad=0.2,rounding_size=0.6", ec="#7c3aed", fc="#7c3aed", lw=0)
    ax.add_patch(c4_hdr)
    ax.text(137, 73, "4. LLM RESPONSE GENERATION", fontsize=10.5, fontweight='bold', ha='center', color='#ffffff')

    ax.text(137, 58, "🤖", fontsize=32, ha='center')
    ax.text(137, 48, "LLM (Llama 3 / Ollama)", fontsize=10, fontweight='bold', ha='center', color='#5b21b6')

    # Dashed line
    ax.plot([124, 150], [44, 44], color='#ddd6fe', lw=1, linestyle='--')

    bbox_ans = patches.FancyBboxPatch((123, 35), 28, 7, boxstyle="round,pad=0.2", ec="#c4b5fd", fc="#ffffff", lw=1)
    ax.add_patch(bbox_ans)
    ax.text(125, 38.5, "💬", fontsize=10)
    ax.text(128, 38.5, "Generate Medical Explanation,\nRecommendations & Precautions", fontsize=7.8, fontweight='bold', color='#374151')

    # Arrows between cards
    ax.annotate('', xy=(44, 54), xytext=(39, 54), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))
    ax.annotate('', xy=(82, 54), xytext=(77, 54), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))
    ax.annotate('', xy=(120, 54), xytext=(115, 54), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))

    # =========================================================================
    # 3. Feedback Loop Arrow
    # =========================================================================
    ax.plot([137, 137, 22.5, 22.5], [32, 24, 24, 32], color="#7c3aed", lw=1.5, linestyle='--')
    ax.annotate('', xy=(22.5, 32), xytext=(22.5, 29), arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=1.5))

    fb_box = patches.FancyBboxPatch((62, 21.5), 36, 5, boxstyle="round,pad=0.3,rounding_size=0.8", ec="#c4b5fd", fc="#ffffff", lw=1.2)
    ax.add_patch(fb_box)
    ax.text(66, 24, "🔄", fontsize=11, ha='center', va='center')
    ax.text(81, 25, "FEEDBACK / FOLLOW-UP", fontsize=8.5, fontweight='bold', color='#5b21b6', ha='center')
    ax.text(81, 22.5, "Ask Follow-up Questions", fontsize=7.5, color='#4b5563', ha='center')

    # =========================================================================
    # 4. Bottom Value Proposition Bar (4 Cards)
    # =========================================================================
    bot_card = patches.FancyBboxPatch((6, 2), 148, 14, boxstyle="round,pad=0.4,rounding_size=0.8", ec="#e2e8f0", fc="#faf5ff", lw=1.2)
    ax.add_patch(bot_card)

    v_props = [
        ("🎯", "ACCURATE\nPREDICTION", "High accuracy deep\nlearning model", 24),
        ("📖", "EVIDENCE-BASED\nINFORMATION", "Retrieves trusted medical\ndocuments", 61),
        ("🛡️", "PERSONALIZED\nRECOMMENDATIONS", "AI-generated explanations\ntailored to the query", 99),
        ("💬", "INTERACTIVE\nAI ASSISTANT", "Ask questions & get instant\nmedical answers", 137)
    ]

    for icon, title, desc, x_pos in v_props:
        ax.text(x_pos - 12, 9, icon, fontsize=16, ha='center', va='center')
        ax.text(x_pos - 7, 10.5, title, fontsize=8.5, fontweight='bold', color='#1e293b')
        ax.text(x_pos - 7, 5.5, desc, fontsize=7.5, color='#64748b')
        if x_pos < 130:
            ax.plot([x_pos + 12, x_pos + 12], [4, 14], color='#e2e8f0', lw=1)

    out_path = "static/images/system_architecture_infographic.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    
    # Save to all target paths
    plt.savefig("static/images/architecture_diagram.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.savefig("static/images/system_architecture.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[SUCCESS] Rendered 1:1 replica infographic at {out_path}")

if __name__ == "__main__":
    draw_exact_infographic()
