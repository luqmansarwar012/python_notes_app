from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .schemas import Token
from .service import login_service
from typing import Annotated
from fastapi import status


router = APIRouter()


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    token: Token = login_service(form_data)
    return token
