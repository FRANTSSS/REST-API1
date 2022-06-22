import os
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Users import Users, DeclarativeBase
from ..excepton import PostgresMethodError
from rest.user.exception import EnvNotFoundError

__all__ = [
    "get_postgres_session"
]


def get_postgres_session() -> Optional[sessionmaker]:
    if os.environ["STORAGE_TYPE"].strip().lower() != "postgres":
        return None
    try:
        str_connect = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASS']}" \
                      f"@{os.environ['POSTGRES_HOST']}:" \
                      f"{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_NAME']}"
    except Exception as e:
        raise EnvNotFoundError(f"env variables not found: {e}")
    try:
        engine = create_engine(str_connect)
        DeclarativeBase.metadata.create_all(engine)
    except Exception as e:
        raise PostgresMethodError(f"Failed to connect database: {e}")
    session = sessionmaker(bind=engine)
    return session
