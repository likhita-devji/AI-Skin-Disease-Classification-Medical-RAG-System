import os
import glob
import logging
import warnings
from typing import List, Dict, Any

# Suppress HuggingFace, pypdf, and sentence-transformers warnings
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
warnings.filterwarnings('ignore')
logging.getLogger("pypdf").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)

class MedicalKnowledgeVectorStore:
    def __init__(self, db_dir: str = "medical_knowledge_db", chroma_persist_dir: str = "chroma_db"):
        self.db_dir = db_dir
        self.chroma_persist_dir = chroma_persist_dir
        self.documents: List[Dict[str, Any]] = []
        self.vector_db = None
        self.use_chroma = False
        self.embedder = None
        self.chroma_client = None
        self.collection = None

        self._initialize_store()

    def _initialize_store(self):
        """Loads medical Markdown and PDF documents, initializing ChromaDB vector store."""
        self._load_all_documents()

        try:
            import chromadb
            from sentence_transformers import SentenceTransformer
            
            self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
            self.chroma_client = chromadb.PersistentClient(path=self.chroma_persist_dir)
            
            self.collection = self.chroma_client.get_or_create_collection(
                name="medical_skin_diseases",
                metadata={"hnsw:space": "cosine"}
            )
            
            if len(self.documents) > 0 and self.embedder is not None:
                ids = [f"doc_{i}" for i in range(len(self.documents))]
                texts = [doc['content'] for doc in self.documents]
                metadatas = [{'source': doc['source'], 'title': doc['title']} for doc in self.documents]
                
                embeddings = self.embedder.encode(texts).tolist()
                self.collection.upsert(
                    ids=ids,
                    embeddings=embeddings,
                    documents=texts,
                    metadatas=metadatas
                )

            self.use_chroma = True
        except Exception:
            self.use_chroma = False

    def _load_all_documents(self):
        """Parse all markdown and PDF files in the medical knowledge directory into structured chunks."""
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir, exist_ok=True)
            return

        # 1. Load Markdown Files (.md)
        md_files = glob.glob(os.path.join(self.db_dir, "*.md"))
        for filepath in md_files:
            filename = os.path.basename(filepath)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                sections = content.split("\n## ")
                doc_title = sections[0].split("\n")[0].replace("#", "").strip() if sections else filename

                for idx, sec in enumerate(sections):
                    chunk_text = ("## " + sec) if idx > 0 else sec
                    if len(chunk_text.strip()) > 50:
                        lines = sec.strip().split("\n")
                        sec_header = lines[0].replace("#", "").strip() if lines else doc_title
                        chunk_title = f"{doc_title} - {sec_header}" if (idx > 0 and sec_header != doc_title) else doc_title
                        
                        self.documents.append({
                            "source": filename,
                            "title": chunk_title,
                            "content": chunk_text.strip()
                        })
            except Exception:
                pass

        # 2. Load PDF Files (.pdf)
        pdf_files = glob.glob(os.path.join(self.db_dir, "*.pdf"))
        for filepath in pdf_files:
            filename = os.path.basename(filepath)
            pdf_chunks = self._read_pdf_file(filepath)
            for page_num, text in enumerate(pdf_chunks, 1):
                if len(text.strip()) > 50:
                    self.documents.append({
                        "source": filename,
                        "title": f"{filename} (Page {page_num})",
                        "content": text.strip()
                    })

    def _read_pdf_file(self, filepath: str) -> List[str]:
        """Extract text page-by-page from a PDF file."""
        chunks = []
        try:
            import pypdf
            reader = pypdf.PdfReader(filepath)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    chunks.append(text)
            return chunks
        except Exception:
            pass

        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(filepath)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    chunks.append(text)
            return chunks
        except Exception:
            pass

        return chunks

    def query(self, query_text: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve top_k relevant medical context chunks for a query."""
        if not self.documents:
            return []

        if self.use_chroma and self.embedder is not None and self.collection is not None:
            try:
                query_embedding = self.embedder.encode([query_text]).tolist()
                results = self.collection.query(
                    query_embeddings=query_embedding,
                    n_results=top_k
                )
                
                retrieved = []
                if results and 'documents' in results and results['documents']:
                    docs = results['documents'][0]
                    metas = results['metadatas'][0] if ('metadatas' in results and results['metadatas']) else [{}]*len(docs)
                    for doc, meta in zip(docs, metas):
                        retrieved.append({
                            "content": doc,
                            "source": meta.get("source", "Medical Reference"),
                            "title": meta.get("title", "Clinical Guide")
                        })
                return retrieved
            except Exception:
                pass

        # Fallback keyword relevance ranker
        query_words = set(query_text.lower().split())
        scored_docs = []
        for doc in self.documents:
            doc_words = set(doc['content'].lower().split())
            overlap = len(query_words.intersection(doc_words))
            scored_docs.append((overlap, doc))

        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored_docs[:top_k]]
