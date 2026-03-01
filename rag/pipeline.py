# ============================================================
# pipeline.py - Pipeline RAG de bout en bout
# ============================================================
# Responsabilités:
#   - Orchestrer l'ensemble du pipeline RAG:
#
#   - Classe RAGPipeline:
#       * __init__(): Initialiser tous les composants
#           - Embedding model (rag/embeddings/model.py)
#           - Vector store (rag/embeddings/store.py)
#           - Retriever (rag/retrieval/retriever.py)
#           - LLM (rag/generation/llm.py)
#           - Chain (rag/generation/chain.py)
#
#       * ingest(documents_path): Pipeline d'ingestion
#           1. Charger les documents (loader.py)
#           2. Chunker les documents (chunker.py)
#           3. Enrichir les métadonnées (metadata.py)
#           4. Générer les embeddings et stocker (store.py)
#
#       * query(question): Pipeline de requête
#           1. Exécuter la chaîne RAG (chain.py)
#           2. Retourner la réponse + sources + métriques
#
#       * get_retriever(): Accéder au retriever configuré
#
#   - Singleton pattern pour réutiliser l'instance
# ============================================================
from rag.ingestion.loader import load_medical_document
from rag.ingestion.chunker import chunk_medical_documents
from rag.embeddings.store import create_vector_store
from rag.generation.chain import create_medical_rag_chain
from rag.retrieval.retriever import get_hybrid_retriever
import mlflow

class RAGPipeline:
    def __init__(self):
        self.chain = None

    @mlflow.trace
    def ingest(self, file_path: str):
        docs = load_medical_document(file_path)
        chunks = chunk_medical_documents(docs)
        

        vector_db = create_vector_store(chunks)
        

        retriever = get_hybrid_retriever(docs)
        self.chain = create_medical_rag_chain(retriever)
        return "System ready: Medical knowledge ingested."

    @mlflow.trace
    def ask(self, question: str):
        """Step 2: The 'Answering' Phase"""
        if not self.chain:
            return "Please ingest documents first."
        

        response = self.chain.invoke({"input": question})
        return response["answer"]