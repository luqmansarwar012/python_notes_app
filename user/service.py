from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, Login
from helpers.id_generator import id_generator


def signup_service(user: UserCreate, db: Session):
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


def login_service(credentials: Login, db: Session):
    find_user = db.query(User).filter(User.username == credentials.username).first()
    if find_user and find_user.password == credentials.password:
        return {"success": True, "token": "DummyToken"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
        )
