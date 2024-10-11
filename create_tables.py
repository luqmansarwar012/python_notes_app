from user.models import User
from note.models import Note
from database import Base, engine
import logging

logging.basicConfig(level=logging.INFO)
try:
    logging.info("Starting to create tables for all models...")
    Base.metadata.create_all(bind=engine)
    logging.info("Tables created successfully!")
except Exception as e:
    logging.error("An error occurred while creating tables!", exc_info=True)
    raise e
