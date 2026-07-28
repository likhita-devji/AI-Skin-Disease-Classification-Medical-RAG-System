"""
Renders a 1:1 high-resolution vector infographic matching the user's exact uploaded image:
'CNN-BASED SKIN DISEASE CLASSIFICATION FLOW'
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_classification_flow_infographic():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # =========================================================================
    # 1. Header Section
    # =========================================================================
    ax.plot([15, 30], [92, 92], color='#0d9488', lw=2)
    ax.scatter([15], [92], color='#0d9488', s=20)
    
    ax.plot([130, 145], [92, 92], color='#0d9488', lw=2)
    ax.scatter([145], [92], color='#0d9488', s=20)

    ax.text(80, 92, "CNN-BASED SKIN DISEASE CLASSIFICATION FLOW", 
            fontsize=20, fontweight='extra bold', ha='center', color='#0f172a')

    ax.text(80, 86, "From skin image input to disease prediction with confidence scores", 
            fontsize=11, ha='center', color='#475569')

    # =========================================================================
    # 2. Four Main Workflow Columns
    # =========================================================================

    # --- Step 1: 1. INPUT IMAGE ---
    ax.text(20, 78, "1. INPUT IMAGE", fontsize=11, fontweight='bold', ha='center', color='#0f766e')
    
    card1 = patches.FancyBboxPatch((6, 36), 28, 38, boxstyle="round,pad=0.5,rounding_size=1", ec="#cbd5e1", fc="#f8fafc", lw=1.2)
    ax.add_patch(card1)
    ax.text(20, 70, "Skin Lesion Image", fontsize=10, fontweight='bold', ha='center', color='#1e293b')
    
    # Image thumbnail placeholder
    thumb_box = patches.Rectangle((9, 44), 22, 22, ec="#cbd5e1", fc="#e2e8f0", lw=1)
    ax.add_patch(thumb_box)
    ax.text(20, 55, "🔬\nSkin Lesion\nSample", fontsize=9, fontweight='bold', ha='center', color='#475569')
    
    ax.text(20, 40, "Formats Supported:\nJPG, PNG, JPEG", fontsize=8.5, ha='center', color='#475569')

    # Arrow 1 -> 2
    ax.annotate('', xy=(37, 55), xytext=(34, 55), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))

    # --- Step 2: 2. PREPROCESSING ---
    ax.text(53, 78, "2. PREPROCESSING", fontsize=11, fontweight='bold', ha='center', color='#0f766e')
    
    card2 = patches.FancyBboxPatch((39, 36), 28, 38, boxstyle="round,pad=0.5,rounding_size=1", ec="#cbd5e1", fc="#f8fafc", lw=1.2)
    ax.add_patch(card2)

    pre_steps = [
        ("⤢", "Resize", "(224 × 224)"),
        ("📊", "Normalize", "Pixel Values"),
        ("📈", "Denoise", "(Noise Reduction)"),
        ("☀️", "Augment", "(Flip, Rotate, Zoom)")
    ]
    for idx, (icon, title, desc) in enumerate(pre_steps):
        y_pos = 66 - (idx * 8.5)
        circ = patches.Circle((44, y_pos + 1.5), 2.5, ec="#0d9488", fc="#ffffff", lw=1.2)
        ax.add_patch(circ)
        ax.text(44, y_pos + 1.5, icon, fontsize=9, ha='center', va='center', color='#0d9488')
        
        ax.text(48, y_pos + 2.5, title, fontsize=9, fontweight='bold', color='#1e293b')
        ax.text(48, y_pos + 0.2, desc, fontsize=7.5, color='#64748b')

    # Arrow 2 -> 3
    ax.annotate('', xy=(70, 55), xytext=(67, 55), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))

    # --- Step 3: 3. CNN MODEL (EfficientNet) ---
    ax.text(88, 78, "3. CNN MODEL", fontsize=11, fontweight='bold', ha='center', color='#0f766e')
    ax.text(88, 74, "(EfficientNet)", fontsize=10, fontweight='bold', ha='center', color='#334155')

    # 3D Feature Maps Graphic Representation
    for idx, (x_c, h_c, w_c, color_c) in enumerate([(72, 22, 5, '#0f766e'), (76, 19, 4.5, '#14b8a6'), (80, 16, 4, '#2dd4bf'), (84, 13, 3.5, '#5eead4'), (88, 10, 3, '#99f6e4')]):
        rect_m = patches.Rectangle((x_c, 44), w_c, h_c, ec="#0f766e", fc=color_c, lw=1)
        ax.add_patch(rect_m)
    
    # Cube layer
    cube = patches.Rectangle((93, 49), 4, 6, ec="#0f766e", fc="#ccfbf1", lw=1)
    ax.add_patch(cube)

    # Arrow to Output Nodes
    ax.annotate('', xy=(100, 52), xytext=(97, 52), arrowprops=dict(arrowstyle="->", color="#0d9488", lw=1.5))

    # Output Node Circles
    node_box = patches.FancyBboxPatch((100.5, 43), 4.5, 18, boxstyle="round,pad=0.2", ec="#0f766e", fc="#f0fdf4", lw=1)
    ax.add_patch(node_box)
    for n_y in [45, 47.5, 50, 52.5, 55, 57.5, 60]:
        nc = patches.Circle((102.75, n_y), 0.8, ec="#0f766e", fc="#14b8a6", lw=1)
        ax.add_patch(nc)

    # Model Highlights Sub-box
    box_hl = patches.FancyBboxPatch((72, 23), 33, 18, boxstyle="round,pad=0.4", ec="#a7f3d0", fc="#f0fdf4", lw=1.2)
    ax.add_patch(box_hl)
    ax.text(88.5, 37.5, "Model Highlights", fontsize=9.5, fontweight='bold', ha='center', color='#065f46')
    
    highlights = [
        "✓ Pre-trained on ImageNet",
        "✓ Transfer Learning",
        "✓ Fine-tuned on Skin Dataset",
        "✓ High Accuracy & Efficiency"
    ]
    for idx, hl in enumerate(highlights):
        ax.text(75, 33.5 - (idx * 3.2), hl, fontsize=8, color='#047857', fontweight='bold')

    # Arrow 3 -> 4
    ax.annotate('', xy=(110, 52), xytext=(105.5, 52), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2))

    # --- Step 4: 4. PREDICTION OUTPUT ---
    ax.text(134, 78, "4. PREDICTION OUTPUT", fontsize=11, fontweight='bold', ha='center', color='#0f766e')

    card4 = patches.FancyBboxPatch((113, 36), 42, 38, boxstyle="round,pad=0.5", ec="#cbd5e1", fc="#ffffff", lw=1.2)
    ax.add_patch(card4)
    hdr4 = patches.FancyBboxPatch((113, 70), 42, 4, boxstyle="round,pad=0.2", ec="#0f766e", fc="#0f766e", lw=0)
    ax.add_patch(hdr4)
    ax.text(134, 72, "Top Predicted Classes", fontsize=10, fontweight='bold', ha='center', color='#ffffff')

    preds = [
        ("🟢 Melanoma", "0.09", False),
        ("🔵 Nevus", "0.71", True),
        ("🟠 Basal Cell Carcinoma", "0.06", False),
        ("🟣 Actinic Keratosis", "0.05", False),
        ("🔴 Vascular Lesions", "0.04", False),
        ("⚪ Others", "0.05", False)
    ]
    for idx, (pname, pval, is_top) in enumerate(preds):
        y_p = 65 - (idx * 4.8)
        if is_top:
            top_bg = patches.Rectangle((114.5, y_p - 1), 39, 4, ec="#bbf7d0", fc="#ecfdf5", lw=0.8)
            ax.add_patch(top_bg)
            ax.text(116, y_p, pname, fontsize=8.5, fontweight='bold', color='#0f172a')
            ax.text(151, y_p, pval, fontsize=8.5, fontweight='bold', color='#0f172a', ha='right')
        else:
            ax.text(116, y_p, pname, fontsize=8, color='#475569')
            ax.text(151, y_p, pval, fontsize=8, color='#475569', ha='right')

    # Arrow to Shield Result Box
    ax.annotate('', xy=(134, 30), xytext=(134, 34), arrowprops=dict(arrowstyle="->", color="#0f172a", lw=1.8))

    # Shield Result Box
    res_shield = patches.FancyBboxPatch((110, 16), 45, 12, boxstyle="round,pad=0.4", ec="#a7f3d0", fc="#f0fdf4", lw=1.5)
    ax.add_patch(res_shield)
    ax.text(115, 22, "🛡️", fontsize=18, va='center')
    ax.text(121, 23.5, "Predicted Disease: ", fontsize=9.5, fontweight='bold', color='#1e293b')
    ax.text(147, 23.5, "Nevus", fontsize=10, fontweight='extra bold', color='#047857')
    ax.text(121, 18.5, "Confidence Score: ", fontsize=9.5, fontweight='bold', color='#1e293b')
    ax.text(147, 18.5, "71%", fontsize=10, fontweight='extra bold', color='#047857')

    # =========================================================================
    # 3. Bottom Legend Bar
    # =========================================================================
    leg_box = patches.FancyBboxPatch((6, 2), 148, 10, boxstyle="round,pad=0.4", ec="#cbd5e1", fc="#ffffff", lw=1, linestyle="--")
    ax.add_patch(leg_box)

    legends = [
        ("#0f766e", "Convolutional Layer", "Extracts features", 12),
        ("#2dd4bf", "Pooling Layer", "Reduces dimensions", 52),
        ("#ccfbf1", "Fully Connected Layer", "High-level reasoning", 92),
        ("#14b8a6", "Output Layer", "Class probabilities", 132)
    ]
    for col, title, desc, x_l in legends:
        icon_leg = patches.Rectangle((x_l, 4.5), 5, 5, ec="#0f766e", fc=col, lw=1)
        ax.add_patch(icon_leg)
        ax.text(x_l + 7, 7.5, title, fontsize=8.5, fontweight='bold', color='#1e293b')
        ax.text(x_l + 7, 4.5, desc, fontsize=7.5, color='#64748b')

    out_path = "static/images/classification_flow_infographic.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    
    # Save to target paths
    plt.savefig("static/images/classification_flow.png", dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"[SUCCESS] Rendered 1:1 Classification Flow Infographic at {out_path}")

if __name__ == "__main__":
    draw_classification_flow_infographic()
