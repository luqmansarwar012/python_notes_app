from fastapi import APIRouter, status
from .schemas import UserCreate, UserResponse
from .service import signup_service

router = APIRouter()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_200_OK)
def signup(user: UserCreate):
    newUser = signup_service(user)
    return newUser
