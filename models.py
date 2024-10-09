from sqlalchemy import String, Integer, Column, ForeignKey
from database import Base, engine

def create_tables():
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(25),nullable = False)
    password = Column(String(10), nullable = False)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key = True)
    title = Column(String(25), nullable = False)
    description = Column(String(80), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)