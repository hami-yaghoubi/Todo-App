from src.schemas.user import UserCreate, UserUpdate
from src.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status



def create_user(user_data : UserCreate, db: Session) -> User :
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
    
    for key, value in update_changes.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    
    return user
    
def delete_user(user_id: int, db: Session) -> None:
    user = get_user(user_id,db)

    db.delete(user)
    db.commit()
