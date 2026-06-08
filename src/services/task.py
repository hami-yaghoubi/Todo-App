from src.schemas.task import TaskCreate, TaskUpdate
from src.models.task import Task
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status
from src.models.user import User


def create_task(task_data : TaskCreate, db: Session, user_id: int) -> Task :
    task = Task(
        title = task_data.title,
        description = task_data.description,
        is_complete = task_data.is_complete,
        user_id = user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_tasks(db: Session, user_id: int) -> list[Task] :
    query = select(Task).where(Task.user_id == user_id)
    result = db.execute(query).scalars().all()

    return result

def get_task(task_id: int ,db: Session, user_id: int) -> Task :
    query = select(Task).where(Task.user_id == user_id, Task.id == task_id)
    task = db.execute(query).scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return task

def update_task(task_id: int, task_data: TaskUpdate, db: Session, user_id: int) -> Task :
    task = get_task(task_id,db,user_id)

    update_changes = task_data.model_dump(exclude_unset=True)
    
    for key, value in update_changes.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    
    return task
    
def delete_task(task_id: int, db: Session, user_id: int) -> None:
    task = get_task(task_id,db,user_id)

    db.delete(task)
    db.commit()
