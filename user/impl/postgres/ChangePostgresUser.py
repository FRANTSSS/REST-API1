from models import User
from user.core import IPostgresMethod
from user.exception import UserNotFoundError
from .Users import Users
from .exception import PostgresMethodError

__all__ = [
    "ChangePostgresUser"
]


class ChangePostgresUser(IPostgresMethod):
    def work(self, uuid=None, full_name=None) -> User:
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
        return User(uuid, full_name)
