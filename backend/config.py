# ============================================================
# config.py - Configuration centralisée (pydantic-settings)
# ============================================================
# Responsabilités:
#   - Charger les variables d'environnement depuis le fichier .env
#   - Définir la classe Settings avec:
#       * DATABASE_URL (PostgreSQL)
#       * SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES (JWT)
#       * EMBEDDING_MODEL_NAME, EMBEDDING_DIMENSION
#       * LLM_MODEL_NAME, LLM_TEMPERATURE, LLM_MAX_TOKENS, LLM_TOP_P, LLM_TOP_K
#       * CHUNK_SIZE, CHUNK_OVERLAP, CHUNKING_STRATEGY
#       * VECTORSTORE_PATH, VECTORSTORE_COLLECTION_NAME
#       * RETRIEVER_K, RETRIEVER_SIMILARITY_METRIC
#       * MLFLOW_TRACKING_URI, MLFLOW_EXPERIMENT_NAME
#       * PROMETHEUS_PORT
#   - Fournir une instance singleton via lru_cache
# ============================================================
