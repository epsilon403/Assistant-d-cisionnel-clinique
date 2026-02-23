# ============================================================
# chain.py - Chaîne RAG LangChain
# ============================================================
# Responsabilités:
#   - Construire la chaîne RAG complète avec LangChain:
#       * RetrievalQA chain ou custom LCEL chain
#       * Combiner: retriever → prompt → LLM → output parser
#   - Pipeline:
#       1. Recevoir la question utilisateur
#       2. (Optionnel) Query expansion
#       3. Retrieval: chercher les chunks pertinents
#       4. (Optionnel) Reranking des chunks
#       5. Construire le prompt avec le contexte
#       6. Générer la réponse via le LLM
#       7. Parser et formater la réponse
#       8. Retourner réponse + sources
#   - Supporter le streaming (optionnel)
# ============================================================
