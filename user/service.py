from fastapi import status, HTTPException, Depends
from .models import User
from .schemas import UserCreate, Login
from database.service import get_db


def signup_service(user: UserCreate):
    db = get_db()
    newUser = User(username=user.username, password=user.password)
    find_user = db.query(User).filter(User.username == user.username).first()
    if find_user:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="User with this username already exists!",
        )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    db.close()
    return newUser


def login_service(credentials: Login):
    db = get_db()
    find_user = db.query(User).filter(User.username == credentials.username).first()
    db.close()
    if find_user and find_user.password == credentials.password:
        return {"success": True, "token": "DummyToken"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
    )
