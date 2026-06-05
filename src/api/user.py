from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users",tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data : UserCreate, db: Session = Depends(get_db)):
    pass


@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    pass

@router.get("/{user_id}", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(user_id: int ,db: Session = Depends(get_db)):
    pass

@router.patch("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    pass

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    pass
