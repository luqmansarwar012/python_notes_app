from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserResponse, Login, LoginResponse
from database import get_db
from helpers.id_generator import id_generator

router = APIRouter()


# User signup
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_200_OK)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    newUser = User(id=id_generator(), username=user.username, password=user.password)
    find_user = db.query(User).filter(User.username == user.username).first()
    if find_user:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="User with this username already exists!",
        )
    db.add(newUser)
    db.commit()
    return newUser


# User login
@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(credentials: Login, db: Session = Depends(get_db)):
    find_user = db.query(User).filter(User.username == credentials.username).first()
    if find_user and find_user.password == credentials.password:
        return {"success": True, "token": "DummyToken"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
        )
