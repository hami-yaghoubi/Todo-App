from fastapi import FastAPI

from src.api.user import router as user_router
from src.api.task import router as task_router

from src.models.user import User
from src.models.task import Task

app = FastAPI(title="Todo API",
              description="Todo Backend With FastAPI")

app.include_router(user_router)
app.include_router(task_router)
