# ============================================================
# store.py - Base de données vectorielle (Vector Store)
# ============================================================
# Responsabilités:
#   - Initialiser la base vectorielle (au choix):
#       * ChromaDB: persistance locale, simple à configurer
#       * FAISS: performant pour les grandes collections
#       * Qdrant: solution cloud-native avec filtrage avancé
#   - Fonctions principales:
#       * create_store(): Créer/initialiser le vector store
#       * add_documents(): Ajouter des documents avec leurs embeddings
#       * persist(): Sauvegarder le store sur disque (data/vectorstore/)
#       * load_store(): Charger un store existant
#       * similarity_search(): Recherche par similarité
#       * delete_collection(): Supprimer une collection
#   - Configuration:
#       * collection_name: nom de la collection
#       * persist_directory: chemin de persistance
#       * distance_metric: cosine, L2, inner_product
# ============================================================

from Langchartin_community.vectorestores import Chroma
import os
from rag.embeddings.model import get_embedding_model
VECTOR_DB_DIR = "data/vectorstore"

def create_vector_store(chunks):
    embadding = get_embedding_model()
    vectore_store = Chroma(
        documents = chunks,
        embadding = embadding,
        collection_name = "medical_docs",
        presist_directory = VECTOR_DB_DIR
    )
    print(f"cextor store created with {len(chunks)} chunks")
    return vectore_store

def load_vector_store():
  
    embeddings = get_embedding_model()
    return Chroma(persist_directory=VECTOR_DB_DIR, embedding_function=embeddings)