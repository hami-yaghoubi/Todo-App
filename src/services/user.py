from src.schemas.user import UserCreate, UserUpdate
from src.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status



def create_user(user_data : UserCreate, db: Session) -> User :
    
    if get_user_by_username(user_data.username, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    user = User(**user_data.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session) -> list[User] :
    query = select(User)
    result = db.execute(query).scalars().all()

    return result

def get_user(user_id: int ,db: Session) -> User :
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

def update_user(user_id: int, user_data: UserUpdate, db: Session) -> User :
    user = get_user(user_id,db)

    update_changes = user_data.model_dump(exclude_unset=True)

    if "username" in update_changes :
        user = get_user_by_username(update_changes["username"], db)
        if user and user.id != user_id:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    for key, value in update_changes.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    
    return user
    
def delete_user(user_id: int, db: Session) -> None:
    user = get_user(user_id,db)

    db.delete(user)
    db.commit()

def get_user_by_username(username:str, db:Session) -> User | None :
    query = select(User).where(User.username == username)
    user = db.execute(query).scalar_one_or_none()

    return user
