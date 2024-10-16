from fastapi import FastAPI
from user import routes as user_routes
from note import routes as note_routes
from database.service import create_tables

create_tables()

app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["User"])
app.include_router(note_routes.router, prefix="/notes", tags=["Notes"])
