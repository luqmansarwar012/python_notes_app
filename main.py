from fastapi import FastAPI
from user import routes as user_routes
from note import routes as note_routes

app = FastAPI()


# Note app end points
app.include_router(user_routes.router, prefix="/user")
app.include_router(note_routes.router, prefix="/note")
