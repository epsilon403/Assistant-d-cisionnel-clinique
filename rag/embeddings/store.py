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
