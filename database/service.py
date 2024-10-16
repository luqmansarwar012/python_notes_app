import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Database configuration
engine = create_engine(DATABASE_URL, echo=True)

# Declarative Base
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


# Create a session instance
def get_db():
    db = SessionLocal()
    return db
    # try:
    #     return db
    # finally:
    #     db.close()


# Logging configuration
logging.basicConfig(level=logging.INFO)


def create_tables():
    try:
        logging.info("Starting to create tables for all models...")
        Base.metadata.create_all(bind=engine)
        logging.info("Tables created successfully!")
    except Exception as e:
        logging.error("An error occurred while creating tables!", exc_info=True)
        raise e
