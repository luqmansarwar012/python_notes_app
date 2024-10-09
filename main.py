from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models
import uuid

# app instance
app = FastAPI()
# db instance
db = SessionLocal()


# User schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    class Config:
        orm_mode = True

# Login schemas
class Login(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    token: str

# Note schemas
class NoteCreate(BaseModel):
    title: str
    description: str
    user_id: int

class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    class Config:
        orm_mode = True

# end-points
# signup
@app.post('/user/signup', response_model = UserResponse, status_code = status.HTTP_200_OK)
def signup(user: UserCreate):
    newUser = models.User(id = generate_id(), username = user.username, password = user.password)
    # check if user with similar id exists
    find_user =  db.query(models.User).filter(models.User.username == user.username).first()
    if find_user:
        raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail = 'User with this username already exists!')
    # add user to database
    db.add(newUser)
    db.commit()
    return newUser

# login 
@app.post('/user/login', response_model = LoginResponse, status_code = status.HTTP_200_OK)
def login(credentials: Login):
    find_user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if find_user and find_user.password == credentials.password: 
        return {'success' :  True, 'token' : "DummyToken"}
    else:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Invalid credentials!')
    

# create note
@app.post('/note/create', response_model = NoteResponse, status_code=status.HTTP_200_OK)
def create_note(note: NoteCreate):
    try:
        user = db.query(models.User).filter(models.User.id == note.user_id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "user with this id not found")
        newNote = models.Note(id = generate_id(), title = note.title, description = note.description, user_id = note.user_id)
        # add note to database
        db.add(newNote)
        db.commit()
        db.refresh(newNote)
        return newNote
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Internal Server Error")

# get notes
@app.get("/note/get/{user_id}", response_model = list[NoteResponse], status_code = status.HTTP_200_OK)
def get_user_notes(user_id: int):
    user_notes = db.query(models.Note).filter(models.Note.user_id == user_id).all()
    if not user_notes:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User notes not found")
    return user_notes

# helper methods
def generate_id() -> int:
    return int(uuid.uuid4().int & 0xffff)


    