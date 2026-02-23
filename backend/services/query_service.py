# ============================================================
# query_service.py - Orchestration des requêtes RAG
# ============================================================
# Responsabilités:
#   - process_query(): Orchestrer l'exécution du pipeline RAG
#       1. Recevoir la question de l'utilisateur
#       2. Appeler le pipeline RAG (retrieval + generation)
#       3. Sauvegarder la query + réponse en base de données
#       4. Logger dans MLFlow (métriques, paramètres)
#       5. Retourner la réponse avec les sources
#   - get_query_history(): Récupérer l'historique des requêtes
#   - get_query_by_id(): Récupérer une requête spécifique
# ============================================================
