from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    username: str = Field(min_length=3,max_length=15)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserUpdate(BaseModel):
    username: str | None = Field(default=None,min_length=3,max_length=15)
