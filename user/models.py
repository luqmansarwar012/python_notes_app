from sqlalchemy import Column, Integer, String
from database.service import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), nullable=False, unique=True)
    password = Column(String(10), nullable=False)
