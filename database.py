from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# database config
engine = create_engine('postgresql://postgres:pg123@localhost/notes_app', echo = True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()