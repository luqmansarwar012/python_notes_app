from sqlalchemy.orm import sessionmaker, declarative_base
from .engine import engine

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


# Create a session instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
