from models import User
from user.core import IPostgresMethod
from user.exception import UserNotFoundError
from .Users import Users

__all__ = [
    "GetPostgresUser"
]


class GetPostgresUser(IPostgresMethod):
    def work(self, uuid=None, full_name=None) -> User:
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception as e:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        return User(uuid, user.full_name)
