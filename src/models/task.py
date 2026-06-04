from src.db.database import Base
from sqlalchemy.orm import mapped_column, Mapped , relationship
from sqlalchemy import String,Text,ForeignKey

class Task(Base):
    __tablename__ = "tasks"
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(255))
    description : Mapped[str | None] = mapped_column(Text, nullable=True)
    is_complete : Mapped[bool] = mapped_column(default=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user : Mapped["User"] = relationship(back_populates="tasks")