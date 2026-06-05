from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks",tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data : TaskCreate, db: Session = Depends(get_db)):
    pass


@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    pass

@router.get("/{task_id}", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(task_id: int ,db: Session = Depends(get_db)):
    pass

@router.patch("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    pass

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    pass
