# ============================================================
# model.py - Configuration du modèle d'embeddings
# ============================================================
# Responsabilités:
#   - Sélectionner et charger le modèle d'embeddings:
#       * HuggingFace: sentence-transformers (all-MiniLM-L6-v2, etc.)
#       * Ollama: modèles locaux (nomic-embed-text, etc.)
#   - Paramètres configurables:
#       * model_name: nom du modèle
#       * dimension: dimensionnalité des vecteurs
#       * normalize: normalisation des embeddings
#   - Fournir une interface unifiée pour générer des embeddings
#   - Supporter le batch embedding pour l'ingestion
# ============================================================
