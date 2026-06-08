from sqlalchemy.orm import Session
from src.core.security import verify_password
from src.services.user import get_user_by_username


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(username,db)

    if not user or not verify_password(password, user.hashed_password):
        return None

    return user

