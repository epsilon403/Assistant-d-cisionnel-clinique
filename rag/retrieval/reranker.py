# ============================================================
# reranker.py - Re-ranking des résultats de recherche
# ============================================================
# Responsabilités:
#   - Ré-ordonner les chunks récupérés par pertinence:
#       * Cross-encoder reranking (ex: ms-marco-MiniLM)
#       * Cohere Rerank API
#       * LLM-based reranking
#   - Intégration avec LangChain ContextualCompressionRetriever
#   - Paramètres:
#       * model_name: modèle de reranking
#       * top_n: nombre de chunks à garder après reranking
#   - Filtrer les chunks non pertinents (score < seuil)
# ============================================================
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors import FlashrankRerank
import os

def get_reranked_retriever(base_retriever, top_n=3):
  
    compressor = FlashrankRerank(model="ms-marco-MiniLM-L-6-v2", top_n=top_n)
    
   
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, 
        base_retriever=base_retriever
    )
    
    return compression_retriever