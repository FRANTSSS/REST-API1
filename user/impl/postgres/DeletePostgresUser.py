from models import User
from user.core import IPostgresMethod
from user.exception import UserNotFoundError
from .Users import Users
from .exception import PostgresMethodError

__all__ = [
    "DeletePostgresUser"
]


class DeletePostgresUser(IPostgresMethod):
    def work(self, uuid=None, full_name=None) -> User:
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        try:
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        return User(uuid)
