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
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from backend.db.base import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())