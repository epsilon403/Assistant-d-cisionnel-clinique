# ============================================================
# session.py - Gestion de l'état de session Streamlit
# ============================================================
# Responsabilités:
#   - Initialiser les variables de session:
#       * token: JWT token
#       * user: informations utilisateur
#       * chat_history: historique de la conversation
#       * is_authenticated: état de connexion
#   - Fonctions utilitaires:
#       * is_logged_in(): Vérifier si l'utilisateur est connecté
#       * set_auth(token, user): Stocker les infos d'auth
#       * clear_auth(): Déconnecter l'utilisateur
#       * add_message(role, content): Ajouter un message au chat
# ============================================================
