import uuid

from sqlalchemy import Column, Uuid, String, Boolean, DateTime, func
from app.configs.database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    body = Column(String, nullable=False)
    archived = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
