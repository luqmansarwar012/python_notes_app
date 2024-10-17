from fastapi import status, HTTPException, Depends
from .models import User
from .schemas import UserCreate, Login
from database.service import get_db
from auth.service import hash_password, verify_password, create_access_token


def signup_service(user: UserCreate):
    db = get_db()
    hashed_password = hash_password(user.password)
    newUser = User(username=user.username, password=hashed_password)
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
    if find_user and verify_password(credentials.password, find_user.password):
        access_token = create_access_token(data={"sub": find_user.username})
        db.close()
        return {"success": True, "token": access_token}

    db.close()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
    )
