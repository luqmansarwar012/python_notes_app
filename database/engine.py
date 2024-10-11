from sqlalchemy import create_engine


# Database configuration
engine = create_engine("postgresql://postgres:pg123@localhost/notes_app", echo=True)
