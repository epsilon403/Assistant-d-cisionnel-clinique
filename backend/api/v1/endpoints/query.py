# ============================================================
# query.py - Endpoints de requêtes RAG
# ============================================================
# Responsabilités:
#   - POST /query/     : Soumettre une question au pipeline RAG
#                        → Reçoit la query, exécute le pipeline RAG,
#                          retourne la réponse générée avec les sources
#                        → Sauvegarde la query et la réponse en DB
#   - GET  /query/     : Lister l'historique des requêtes de l'utilisateur
#   - GET  /query/{id} : Récupérer une requête spécifique avec sa réponse
# ============================================================
