# ============================================================
# retriever.py - Configuration du retriever
# ============================================================
# Responsabilités:
#   - Configurer le retriever LangChain à partir du vector store
#   - Paramètres:
#       * search_type: "similarity", "mmr" (Maximal Marginal Relevance)
#       * k: nombre de chunks à retourner (ex: 4, 6, 10)
#       * score_threshold: seuil minimum de similarité
#       * filter: filtres sur les métadonnées
#   - Supporter plusieurs types de retrievers:
#       * VectorStoreRetriever (base)
#       * ContextualCompressionRetriever (avec reranker)
#       * EnsembleRetriever (combinaison de retrievers)
#       * MultiQueryRetriever (query expansion automatique)
# ============================================================
