# ============================================================
# metrics.py - Middleware Prometheus pour FastAPI
# ============================================================
# Responsabilités:
#   - Collecter les métriques applicatives:
#       * request_count: Nombre total de requêtes (par endpoint, méthode, status)
#       * request_latency: Latence des requêtes (histogram)
#       * rag_query_count: Nombre de requêtes RAG
#       * rag_query_latency: Latence du pipeline RAG
#       * rag_retrieval_latency: Latence de la phase retrieval
#       * rag_generation_latency: Latence de la phase generation
#       * rag_error_count: Nombre d'erreurs RAG
#       * active_requests: Requêtes en cours (gauge)
#   - Exposer l'endpoint /metrics pour Prometheus
# ============================================================
