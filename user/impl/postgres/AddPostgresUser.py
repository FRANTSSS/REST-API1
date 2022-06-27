from uuid import uuid4

from models import User
from user.core import IPostgresMethod
from .Users import Users
from .exception import PostgresMethodError

__all__ = [
    "AddPostgresUser"
]


class AddPostgresUser(IPostgresMethod):
    def work(self, uuid=None, full_name=None) -> User:
        uuid = uuid4()
        user = Users(
            uuid=str(uuid),
            full_name=full_name)
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        return user
