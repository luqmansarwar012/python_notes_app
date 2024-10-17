from sqlalchemy import Column, Integer, String, ForeignKey
from database.service import Base


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    description = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
