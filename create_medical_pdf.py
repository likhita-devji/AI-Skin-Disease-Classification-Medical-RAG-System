"""
Script to build a comprehensive Medical PDF Reference Guide in medical_knowledge_db/
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_dermatology_pdf():
    pdf_path = "medical_knowledge_db/Dermatology_Clinical_Reference_Guide.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        textColor=colors.HexColor('#005580'),
        spaceAfter=15
    )
    
    h2_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.HexColor('#008080'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#222222'),
        spaceAfter=8
    )

    story = []
    story.append(Paragraph("Clinical Dermatology Reference Guide for Skin Lesions", title_style))
    story.append(Paragraph("Official Medical Reference Textbook & Guidelines for AI Medical RAG System", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#005580'), spaceAfter=15))

    sections = [
        ("1. Melanoma (MEL)", [
            "Melanoma is the most aggressive form of skin cancer, originating in melanocytes.",
            "Diagnostic Rule - ABCDE: Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolving shape/size.",
            "Subtypes: Superficial Spreading Melanoma, Nodular Melanoma, Lentigo Maligna Melanoma, Acral Lentiginous Melanoma.",
            "Treatment Protocol: Excisional wide local surgery, sentinel lymph node biopsy, immunotherapy (Pembrolizumab), targeted BRAF inhibitors."
        ]),
        ("2. Basal Cell Carcinoma (BCC)", [
            "Most common malignant skin cancer in humans worldwide. Expand slowly with low metastasis (<0.1%) but high local tissue destruction.",
            "Clinical Presentation: Pearly nodule with rolled borders, arborizing blood vessels (telangiectasias), central ulceration.",
            "Treatment: Mohs Micrographic Surgery (cure rate >99%), standard surgical excision, cryotherapy, topical 5-FU."
        ]),
        ("3. Actinic Keratosis (AKIEC)", [
            "Pre-cancerous sun-damaged skin lesion with potential to progress into Invasive Squamous Cell Carcinoma (5-10%).",
            "Symptoms: Rough, sand-paper-like scaly patch on forehead, balding scalp, ears, or forearms.",
            "Interventions: Liquid nitrogen cryotherapy, topical 5-Fluorouracil, Imiquimod cream, Photodynamic Therapy (PDT)."
        ]),
        ("4. Benign Keratosis-like Lesions (BKL)", [
            "Non-cancerous epidermal growths including Seborrheic Keratoses and Solar Lentigines (sun spots).",
            "Appearance: Waxy, stuck-on or pasted-on surface with comedo-like openings and keratin cysts.",
            "Management: Entirely benign with zero malignant potential. Removal for cosmetic reasons only via cryotherapy or shave biopsy."
        ]),
        ("5. Dermatofibroma (DF)", [
            "Benign fibrous dermal nodule common on lower legs. Exhibits positive Fitzpatrick Pinch Sign (dimples inward when pinched).",
            "Etiology: Triggered by minor trauma or insect bites. Asymptomatic and benign."
        ]),
        ("6. Melanocytic Nevi (NV) - Common Moles", [
            "Benign clusters of melanocytes. Classified into Junctional, Compound, and Intradermal nevi.",
            "Monitoring: Track for 'Ugly Duckling' sign and sudden changes using monthly self-exams."
        ]),
        ("7. Vascular Lesions (VASC)", [
            "Lesions arising from blood vessels, including Cherry Angiomas, Pyogenic Granulomas, and Hemangiomas.",
            "Diagnosis: Diascopy blanching test. Benign capillary growths."
        ])
    ]

    for title, paragraphs in sections:
        story.append(Paragraph(title, h2_style))
        for p in paragraphs:
            story.append(Paragraph(p, body_style))
        story.append(Spacer(1, 6))

    doc.build(story)
    print(f"[PDF Generator] Successfully created medical PDF reference guide at {pdf_path}")

if __name__ == "__main__":
    create_dermatology_pdf()
