from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.schemas.user import UserCreate, UserResponse, UserUpdate
import src.services.user as user_services
from src.models.user import User
from src.dependencies.auth import get_current_user
from src.dependencies.database import get_db

router = APIRouter(prefix="/users",tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data : UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(user_data, db)

@router.get("/all", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user_services.get_users(db)

@router.get("/", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_services.get_user(current_user.id, db)

@router.patch("/", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_services.update_user(current_user.id, user_data, db)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_services.delete_user(current_user.id, db)
