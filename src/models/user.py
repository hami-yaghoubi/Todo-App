from src.db.database import Base
from sqlalchemy.orm import mapped_column, Mapped , relationship
from sqlalchemy import String

print(Base)

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(255))
    tasks : Mapped[list["Task"]] = relationship(back_populates="user")