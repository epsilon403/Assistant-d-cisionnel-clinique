# ============================================================
# deps.py - Dépendances FastAPI (Dependency Injection)
# ============================================================
# Responsabilités:
#   - get_db(): Fournir une session SQLAlchemy par requête
#   - get_current_user(): Valider le token JWT et retourner l'utilisateur courant
#   - get_rag_pipeline(): Fournir l'instance du pipeline RAG
#   - role_required(): Vérifier le rôle de l'utilisateur (admin, médecin)
# ============================================================
