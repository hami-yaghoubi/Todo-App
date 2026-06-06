from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.user import UserCreate, UserResponse, UserUpdate
import src.services.user as user_services

router = APIRouter(prefix="/users",tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data : UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(user_data, db)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user_services.get_users(db)

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int ,db: Session = Depends(get_db)):
    return user_services.get_user(user_id, db)

@router.patch("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    return user_services.update_user(user_id, user_data, db)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_services.delete_user(user_id, db)
