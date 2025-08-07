import os

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(url=DATABASE_URL)
session_maker = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False, autocommit=False)


def get_session():
    session = session_maker()

    try:
        yield session
    finally:
        session.close()
