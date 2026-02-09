from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import Depends


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DATABASE_URL = "sqlite:///db.sqlite3"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":
    False}
)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)