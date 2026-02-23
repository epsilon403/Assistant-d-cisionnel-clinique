# ============================================================
# api_client.py - Client HTTP pour communiquer avec le backend
# ============================================================
# Responsabilités:
#   - Classe ApiClient avec méthodes pour chaque endpoint:
#       * login(email, password) → token
#       * register(username, email, password, role)
#       * get_me(token) → user info
#       * submit_query(token, question) → RAG response
#       * get_history(token) → list of queries
#       * get_query(token, query_id) → query detail
#   - Gérer les headers d'authentification (Bearer token)
#   - Gérer les erreurs HTTP et les afficher
#   - Base URL configurable (BACKEND_URL)
# ============================================================
