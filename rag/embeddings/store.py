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

from langchain_chroma import Chroma
import os
import mlflow
from rag.embeddings.model import get_embedding_model
VECTOR_DB_DIR = "data/vectorstore"

@mlflow.trace
def create_vector_store(chunks):
    embedding = get_embedding_model()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        collection_name="medical_docs",
        persist_directory=VECTOR_DB_DIR
    )
    print(f"Vector store created with {len(chunks)} chunks")
    return vector_store

@mlflow.trace
def load_vector_store():
  
    embeddings = get_embedding_model()
    return Chroma(
        persist_directory=VECTOR_DB_DIR,
        collection_name="medical_docs",
        embedding_function=embeddings
    )