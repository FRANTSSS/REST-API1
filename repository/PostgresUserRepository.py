from uuid import uuid4

from sqlalchemy.orm import sessionmaker

from models import User
from repository.exception import PostgresMethodError
from repository.exception import UserNotFoundError
from .IUserRepository import IUserRepository
from .Users import Users

__all__ = [
    "PostgresUserRepository"
]


class PostgresUserRepository(IUserRepository):
    def __init__(self, session: sessionmaker):
        self.session = session()

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