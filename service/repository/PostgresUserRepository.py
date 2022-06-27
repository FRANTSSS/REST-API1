from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import EnvDTO
from models import User
from service.exception import PostgresMethodError
from service.exception import UserNotFoundError
from .IUserRepository import IUserRepository
from .Users import DeclarativeBase
from .Users import Users

__all__ = [
    "PostgresUserRepository"
]


class PostgresUserRepository(IUserRepository):
    def __init__(self, env: EnvDTO):
        str_connect = f"postgresql+psycopg2://{env.database_user}:{env.database_password}" \
                      f"@{env.database_host}:" \
                      f"{env.database_port}/{env.database_name}"
        try:
            engine = create_engine(str_connect)
            DeclarativeBase.metadata.create_all(engine)
        except Exception as e:
            raise PostgresMethodError(f"Failed to connect database: {e}")
        self.session = Session(bind=engine)

    def add(self, full_name: str) -> User:
        uuid = str(uuid4())
        user = Users(
            uuid=str(uuid),
            full_name=full_name)
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        return user

    def get(self, uuid: str) -> User:
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception as e:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        return User(uuid, user.full_name)

    def update(self, uuid: str, full_name):
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
            user.full_name = full_name
        except Exception:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")

    def delete(self, uuid: str):
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        try:
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")