from fastapi import status, HTTPException
from .models import User
from .schemas import UserCreate
from database.service import get_db
from auth.service import hash_password


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
