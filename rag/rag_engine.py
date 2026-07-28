import os
import requests
import json
from typing import Dict, Any, List
from rag.vector_store import MedicalKnowledgeVectorStore

class SkinDiseaseRAGEngine:
    def __init__(self, ollama_url: str = None, model_name: str = "llama3:latest"):
        self.ollama_url = ollama_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model_name = model_name
        self.vector_store = MedicalKnowledgeVectorStore()

    def generate_response(self, user_query: str, predicted_disease_code: str = None, disease_info: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Combines retrieved medical literature with user query and disease prediction
        to generate a grounded, safe medical response including Cure & Treatment protocols.
        """
        disease_name = disease_info.get("name", "") if disease_info else ""
        search_prompt = f"{disease_name} cure treatment medical procedures remedies {user_query}".strip()
        
        # 1. Retrieve context chunks from VectorStore (both PDF & MD)
        context_chunks = self.vector_store.query(search_prompt, top_k=3)
        context_text = "\n\n".join([f"--- Source: {c['source']} ({c['title']}) ---\n{c['content']}" for c in context_chunks])

        # 2. Check if local Ollama service is responsive
        ollama_active = self._check_ollama_status()

        if ollama_active:
            system_prompt = (
                "You are an expert AI Medical Assistant specializing in Clinical Dermatology. "
                "Your responses MUST be grounded ONLY in the provided verified clinical reference guides. "
                "Always include a detailed section on 'How to Cure & Treat' (clinical procedures, surgeries, topical medications, home care). "
                "Do NOT hallucinate unverified medical claims. Recommend consulting a board-certified dermatologist."
            )
            
            user_prompt = (
                f"Predicted Condition: {disease_name}\n"
                f"User Question: {user_query}\n\n"
                f"Retrieved Clinical Medical Knowledge (PDFs & Guides):\n{context_text}\n\n"
                "Please provide a comprehensive response covering:\n"
                "1. Overview & Clinical Symptoms\n"
                "2. How to Cure & Medical Treatment Plan (Surgical procedures, topical creams, cure rates)\n"
                "3. Patient Self-Care & Precautions\n"
                "4. When to See a Dermatologist"
            )
            
            try:
                response = requests.post(
                    f"{self.ollama_url}/api/generate",
                    json={
                        "model": self.model_name,
                        "system": system_prompt,
                        "prompt": user_prompt,
                        "stream": False
                    },
                    timeout=10
                )
                if response.status_code == 200:
                    answer_text = response.json().get("response", "")
                    return {
                        "response": answer_text,
                        "grounded_sources": [c['source'] for c in context_chunks],
                        "llm_engine": f"Ollama ({self.model_name})"
                    }
            except Exception as e:
                print(f"[RAG Engine] Ollama connection error: {e}. Using grounded template engine.")

        # 3. Fallback Grounded Synthesis Engine with Cure & Treatment Details
        fallback_answer = self._synthesize_grounded_fallback(user_query, disease_name, disease_info, context_chunks)
        return {
            "response": fallback_answer,
            "grounded_sources": [c['source'] for c in context_chunks],
            "llm_engine": "Clinical Knowledge RAG Engine (PDF & Markdown Medical Literature)"
        }

    def _check_ollama_status(self) -> bool:
        """Check if local Ollama server is running."""
        try:
            res = requests.get(f"{self.ollama_url}/api/tags", timeout=1.5)
            return res.status_code == 200
        except Exception:
            return False

    def _synthesize_grounded_fallback(self, query: str, disease_name: str, disease_info: Dict[str, Any], chunks: List[Dict[str, Any]]) -> str:
        """Generates a structured, clinical summary including Cure & Treatment protocols."""
        lines = []
        if disease_info:
            lines.append(f"### 📋 Diagnostic Insights for {disease_info.get('name', 'Predicted Condition')}")
            lines.append(f"**Category:** {disease_info.get('category', 'Dermatological condition')}")
            lines.append(f"**Severity Rating:** {disease_info.get('severity', 'Medical evaluation recommended')}")
            lines.append(f"**Overview:** {disease_info.get('description', '')}\n")

        lines.append("### 💊 How to Cure & Medical Treatment Plan")
        treatments = self._get_cure_protocol(disease_info.get("prediction_code") if disease_info else "")
        for t in treatments:
            lines.append(f"- **{t['heading']}:** {t['detail']}")

        lines.append("\n### 🩺 Grounded Clinical Medical Literature")
        if chunks:
            for idx, c in enumerate(chunks, 1):
                lines.append(f"**Section {idx} ({c['title']} - {c['source']}):**")
                lines.append(c['content'])
                lines.append("")
        else:
            lines.append("Standard dermatological evaluation guidelines recommend monitoring skin lesions using the ABCDE criteria and avoiding prolonged UV exposure.")

        lines.append("\n### ⚠️ Patient Self-Care & Precautions")
        if disease_info and disease_info.get('immediate_advice'):
            lines.append(f"- {disease_info.get('immediate_advice')}")
        lines.append("- Perform monthly self-examinations to track changes in size, shape, or color.")
        lines.append("- Consult a board-certified dermatologist for formal dermoscopic evaluation or biopsy.")
        
        return "\n".join(lines)

    def _get_cure_protocol(self, code: str) -> List[Dict[str, str]]:
        """Returns specific curative procedures and treatment plans for skin conditions."""
        protocols = {
            "mel": [
                {"heading": "Surgical Wide Local Excision", "detail": "Curative in early-stage localized melanoma (Stage I & II). Removes tumor with safe 1-2cm margins."},
                {"heading": "Sentinel Lymph Node Biopsy (SLNB)", "detail": "Evaluates lymph node spread for lesions with Breslow thickness >0.8mm."},
                {"heading": "Targeted Immunotherapy", "detail": "Pembrolizumab or Nivolumab checkpoint inhibitors; BRAF/MEK inhibitors (Dabrafenib + Trametinib) for BRAF mutations."}
            ],
            "bcc": [
                {"heading": "Mohs Micrographic Surgery (MMS)", "detail": "Gold-standard curative procedure with >99% cure rate for facial or high-risk BCCs."},
                {"heading": "Standard Excision", "detail": "Complete surgical removal with 4mm margins for low-risk trunk/limb BCCs."},
                {"heading": "Topical & Cryotherapy", "detail": "5-Fluorouracil (5-FU) cream or Liquid Nitrogen freezing for superficial BCC."}
            ],
            "akiec": [
                {"heading": "Cryotherapy (Liquid Nitrogen)", "detail": "First-line freezing treatment to destroy pre-cancerous dysplastic cells."},
                {"heading": "Topical Field Chemotherapy", "detail": "Efudex (5-FU 5%) cream or Imiquimod cream applied over 2-4 weeks."},
                {"heading": "Photodynamic Therapy (PDT)", "detail": "Application of photosensitizer followed by light therapy to eradicate lesions."}
            ],
            "bkl": [
                {"heading": "Cryosurgery or Shave Removal", "detail": "Benign condition; curable/removable via quick freezing or shave excision if cosmetically desired."},
                {"heading": "Electrocautery / Laser Ablation", "detail": "Burns away waxy seborrheic keratosis growths with minimal scarring."}
            ],
            "df": [
                {"heading": "Full-Thickness Dermal Excision", "detail": "Complete surgical removal if painful or frequently traumatized during shaving."},
                {"heading": "Liquid Nitrogen Cryo-flattening", "detail": "Flattens raised nodules if surgery is not preferred."}
            ],
            "nv": [
                {"heading": "Excisional Biopsy", "detail": "Complete removal of atypical or changing moles for histopathological analysis."},
                {"heading": "Monitoring", "detail": "Benign moles require no treatment; routine self-exams using ABCDE guidelines."}
            ],
            "vasc": [
                {"heading": "Pulsed Dye Laser (PDL) & IPL", "detail": "Targeted light therapy selectively closes abnormal blood vessels with high cosmetic success."},
                {"heading": "Electrocautery / Curettage", "detail": "Effective removal for pyogenic granulomas or bleeding cherry angiomas."}
            ]
        }
        return protocols.get(code, [
            {"heading": "Dermatological Evaluation", "detail": "Consult a certified dermatologist for personalized prescription creams, laser therapy, or minor surgical excision."},
            {"heading": "Topical Medical Care", "detail": "Apply prescribed medicated creams and maintain daily broad-spectrum sun protection (SPF 50+)."}
        ])
