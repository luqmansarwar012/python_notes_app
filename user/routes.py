from fastapi import APIRouter, status, BackgroundTasks
from .schemas import UserCreate, UserResponse
from .service import signup_service

router = APIRouter()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_200_OK)
def signup(user: UserCreate, background_tasks: BackgroundTasks):
    newUser = signup_service(user, background_tasks)
    return newUser
