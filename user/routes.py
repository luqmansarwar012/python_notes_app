from fastapi import APIRouter, status
from .schemas import UserCreate, UserResponse, Login, LoginResponse
from .service import signup_service, login_service

router = APIRouter()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_200_OK)
def signup(user: UserCreate):
    newUser = signup_service(user)
    return newUser


@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(credentials: Login):
    return login_service(credentials)
