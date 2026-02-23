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
