from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from src.schemas.task import TaskCreate, TaskResponse, TaskUpdate
import src.services.task as task_services
from src.models.user import User
from src.dependencies.auth import get_current_user
from src.dependencies.database import get_db


router = APIRouter(prefix="/tasks",tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data : TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_services.create_task(task_data, db, current_user.id)

@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_services.get_tasks(db, current_user.id)

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id: int ,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_services.get_task(task_id, db, current_user.id)

@router.patch("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_services.update_task(task_id, task_data, db, current_user.id)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_services.delete_task(task_id,db, current_user.id)
