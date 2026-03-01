from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from backend.db.base import Base


class Query(Base):
    __tablename__ = "Query"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(Text, nullable=False)
    reponse = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))