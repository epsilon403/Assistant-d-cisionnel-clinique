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
