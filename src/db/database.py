from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():
    with SessionLocal() as session:
        yield session