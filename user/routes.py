from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserResponse, Login, LoginResponse
from database.service import get_db
from .service import signup_service, login_service

router = APIRouter()


# User signup
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_200_OK)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    newUser = signup_service(user, db)
    return newUser


# User login
@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(credentials: Login, db: Session = Depends(get_db)):
    login_service(credentials, db)
