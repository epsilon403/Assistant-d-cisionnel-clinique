# ============================================================
# user.py - Modèle SQLAlchemy User
# ============================================================
# Table: users
# Colonnes:
#   - id: Integer, Primary Key, auto-increment
#   - username: String, unique, not null
#   - email: String, unique, not null
#   - hashed_password: String, not null
#   - role: String, not null (ex: "admin", "médecin")
#   - created_at: DateTime, default=now
#   - updated_at: DateTime, onupdate=now
# ============================================================
