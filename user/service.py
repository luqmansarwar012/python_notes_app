from fastapi import status, HTTPException, BackgroundTasks
from auth.service import hash_password
from database.service import get_db
from .schemas import UserCreate
from .models import User
from common.email_service import send_email


def signup_service(user: UserCreate, background_tasks: BackgroundTasks):
    db = get_db()
    hashed_password = hash_password(user.password)
    newUser = User(username=user.username, password=hashed_password, email=user.email)
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
    background_tasks.add_task(send_email, newUser.email, newUser.username)
    return newUser
