from pydantic import BaseModel, Field, ConfigDict


class TaskBase(BaseModel):
    title: str = Field(min_length=3,max_length=255)
    description: str | None = Field(default=None,max_length=1000)
    is_complete: bool = Field(default=False)

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None,min_length=3,max_length=255)
    description: str | None = Field(default=None,max_length=1000)
    is_complete: bool | None = None