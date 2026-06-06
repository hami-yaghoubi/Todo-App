from src.schemas.task import TaskCreate, TaskUpdate
from src.models.task import Task
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException



def create_task(task_data : TaskCreate, db: Session) -> Task :
    task = task(**task_data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_tasks(db: Session) -> list[Task] :
    query = select(Task)
    result = db.execute(query).scalars().all()

    return result

def get_task(task_id: int ,db: Session) -> Task :
    task = db.get(task, task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    return task

def update_task(task_id: int, task_data: TaskUpdate, db: Session) -> Task :
    task = get_task(task_id,db)

    update_changes = task_data.model_dump(exclude_unset=True)
    
    for key, value in update_changes.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    
    return task
    
def delete_task(task_id: int, db: Session) -> None:
    task = get_task(task_id,db)

    db.delete(task)
    db.commit()
