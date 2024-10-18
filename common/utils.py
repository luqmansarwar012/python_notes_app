from database.service import get_db
from user.models import User


def get_user(user_id: int):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user
