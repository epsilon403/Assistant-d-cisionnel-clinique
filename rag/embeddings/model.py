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
from langchain_community.embeddings import HugginFaceEmbeddings
import os

def get_embedding_model():
    embedding_model = HugginFaceEmbeddings(model_name=os.getenv('EMBEDDING_MODEL' , 'sentence-transformsers/all-MiniLLM-L6-v2'))
    return embedding_model