from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    fullname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(15), nullable=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)