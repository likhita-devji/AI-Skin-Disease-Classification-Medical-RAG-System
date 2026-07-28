"""
Renders a 1:1 high-resolution vector infographic matching the user's exact uploaded image:
'3. MEDICAL RAG PIPELINE - Retrieval-Augmented Generation for Evidence-Based Medical Answers'
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_rag_pipeline_infographic():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # =========================================================================
    # 1. Header Section
    # =========================================================================
    ax.text(80, 94, "3. MEDICAL RAG PIPELINE", 
            fontsize=20, fontweight='extra bold', ha='center', color='#0f172a')

    # Subtitle line
    ax.plot([45, 115], [88, 88], color='#8b5cf6', lw=1.5)
    ax.scatter([45, 115], [88, 88], color='#8b5cf6', s=20, zorder=5)
    ax.text(80, 88, " Retrieval-Augmented Generation for Evidence-Based Medical Answers ", fontsize=10.5, fontweight='bold', ha='center', color='#7c3aed', backgroundcolor='#ffffff')

    # =========================================================================
    # 2. Six Sequential Step Cards
    # =========================================================================
    
    steps = [
        ("1", "INGEST", "📄", "Medical Documents", ["• Research Papers", "• Guidelines", "• Textbooks", "• Web Resources"], "#9333ea", "#faf5ff", "#c084fc", 6),
        ("2", "CHUNK", "📜", "Text Chunking", ["Split documents into", "small, meaningful", "chunks"], "#2563eb", "#eff6ff", "#93c5fd", 31),
        ("3", "EMBED", "🕸️", "Generate Embeddings", ["Convert chunks into", "vector embeddings", "using embedding model"], "#16a34a", "#f0fdf4", "#86efac", 56),
        ("4", "STORE", "🛢️", "Vector Database\n(ChromaDB)", ["Store embeddings for", "fast and efficient", "similarity search"], "#ea580c", "#fff7ed", "#fed7aa", 81),
        ("5", "RETRIEVE", "🔍", "Retriever", ["Search and retrieve", "top-k relevant chunks", "based on the query"], "#db2777", "#fdf2f8", "#fbcfe8", 106),
        ("6", "GENERATE", "🧠", "LLM Generation", ["LLM uses retrieved", "context to generate", "accurate medical", "answers"], "#1d4ed8", "#eff6ff", "#bfdbfe", 131)
    ]

    for num, tag, icon, title, desc_lines, col_main, col_bg, col_border, x_p in steps:
        # Step number badge circle
        num_circ = patches.Circle((x_p + 11.5, 78), 2.5, ec=col_main, fc=col_main, lw=1)
        ax.add_patch(num_circ)
        ax.text(x_p + 11.5, 78, num, fontsize=10, fontweight='bold', ha='center', va='center', color='#ffffff')
        
        # Step Tag
        ax.text(x_p + 11.5, 73, tag, fontsize=9.5, fontweight='bold', ha='center', color=col_main)

        # Card container
        card_step = patches.FancyBboxPatch((x_p, 36), 23, 34, boxstyle="round,pad=0.4", ec=col_border, fc=col_bg, lw=1.2)
        ax.add_patch(card_step)

        # Icon box inside
        ibox = patches.FancyBboxPatch((x_p + 3, 55), 17, 12, boxstyle="round,pad=0.2", ec="#cbd5e1", fc="#ffffff", lw=1)
        ax.add_patch(ibox)
        ax.text(x_p + 11.5, 61, icon, fontsize=18, ha='center', va='center')

        # Title
        ax.text(x_p + 11.5, 50, title, fontsize=8.5, fontweight='bold', ha='center', color='#1e293b')

        # Description lines
        for l_idx, dline in enumerate(desc_lines):
            ax.text(x_p + 11.5, 44 - (l_idx * 3), dline, fontsize=7.5, color='#475569', ha='center')

        # Arrow to next step
        if x_p < 130:
            ax.annotate('', xy=(x_p + 26, 53), xytext=(x_p + 23.5, 53), arrowprops=dict(arrowstyle="->", color=col_main, lw=1.8))

    # =========================================================================
    # 3. Data Sources Box (Bottom Left)
    # =========================================================================
    box_ds = patches.FancyBboxPatch((6, 16), 78, 16, boxstyle="round,pad=0.4", ec="#c4b5fd", fc="#faf5ff", lw=1.2)
    ax.add_patch(box_ds)
    ax.text(45, 29, "DATA SOURCES", fontsize=9.5, fontweight='bold', ha='center', color='#6d28d9')

    ds_items = [
        ("📖", "Medical\nTextbooks", 14),
        ("📄", "Clinical\nGuidelines", 29),
        ("🎓", "Research\nPapers", 44),
        ("🌐", "Web\nResources", 59),
        ("🛢️", "Internal\nKnowledge", 74)
    ]
    for icon, lbl, x_d in ds_items:
        ax.text(x_d, 22, icon, fontsize=14, ha='center')
        ax.text(x_d, 18, lbl, fontsize=7.5, fontweight='bold', color='#334155', ha='center')

    # Arrow from Data Sources -> User Query
    ax.annotate('', xy=(88, 24), xytext=(85, 24), arrowprops=dict(arrowstyle="->", color="#6d28d9", lw=1.8))

    # User Query Box
    box_uq = patches.FancyBboxPatch((89, 16), 33, 16, boxstyle="round,pad=0.4", ec="#c4b5fd", fc="#ffffff", lw=1.2, linestyle="--")
    ax.add_patch(box_uq)
    ax.text(105.5, 29, "USER QUERY", fontsize=9, fontweight='bold', ha='center', color='#6d28d9')
    ax.text(93, 22, "❓", fontsize=14)
    ax.text(97, 22, "e.g., \"What are the\ntreatment options for\nMelanoma?\"", fontsize=7.8, color='#334155', fontweight='bold')

    # Arrow pointing from User Query UP to 5. RETRIEVE
    ax.annotate('', xy=(117.5, 36), xytext=(117.5, 26), arrowprops=dict(arrowstyle="->", color="#db2777", lw=1.8))

    # Response Box (Bottom Right)
    box_resp = patches.FancyBboxPatch((124, 16), 30, 16, boxstyle="round,pad=0.4", ec="#86efac", fc="#f0fdf4", lw=1.2)
    ax.add_patch(box_resp)
    ax.text(139, 29, "RESPONSE", fontsize=9.5, fontweight='bold', ha='center', color='#15803d')
    ax.text(128, 22, "✅", fontsize=14)
    ax.text(133, 22, "Evidence-based answer\nwith references from\ntrusted medical sources.", fontsize=7.8, color='#14532d', fontweight='bold')

    # Arrow pointing down from 6. GENERATE to RESPONSE
    ax.annotate('', xy=(139, 32), xytext=(139, 36), arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=1.8))

    # =========================================================================
    # 4. Benefits of Medical RAG (Very Bottom Bar)
    # =========================================================================
    bot_bar = patches.FancyBboxPatch((6, 2), 148, 11, boxstyle="round,pad=0.4", ec="#bfdbfe", fc="#eff6ff", lw=1.2)
    ax.add_patch(bot_bar)

    ax.text(80, 10.5, "BENEFITS OF MEDICAL RAG", fontsize=9.5, fontweight='bold', ha='center', color='#1e40af')

    benefits = [
        ("🛡️", "Evidence-Based\nResponses", 24),
        ("🎯", "Reduces Hallucinations\n& Improves Accuracy", 63),
        ("🕒", "Up-to-Date\nKnowledge Retrieval", 102),
        ("👥", "Trustworthy &\nExplainable AI", 138)
    ]
    for icon, label, x_b in benefits:
        ax.text(x_b - 12, 5.5, icon, fontsize=14, ha='center')
        ax.text(x_b - 7, 5.5, label, fontsize=8, fontweight='bold', color='#1e293b')
        if x_b < 130:
            ax.plot([x_b + 12, x_b + 12], [3, 9], color='#cbd5e1', lw=1)

    out_path = "static/images/medical_rag_pipeline_infographic.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    
    # Also save as rag_pipeline.png
    plt.savefig("static/images/rag_pipeline.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[SUCCESS] Rendered 1:1 Medical RAG Pipeline Infographic at {out_path}")

if __name__ == "__main__":
    draw_rag_pipeline_infographic()
