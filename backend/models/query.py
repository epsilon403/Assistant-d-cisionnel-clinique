# ============================================================
# query.py - Modèle SQLAlchemy Query
# ============================================================
# Table: queries
# Colonnes:
#   - id: Integer, Primary Key, auto-increment
#   - user_id: Integer, Foreign Key → users.id
#   - query: Text, not null
#   - reponse: Text, not null
#   - sources: JSON (liste des chunks sources utilisés)
#   - created_at: DateTime, default=now
# Relations:
#   - user: relationship → User
# ============================================================
