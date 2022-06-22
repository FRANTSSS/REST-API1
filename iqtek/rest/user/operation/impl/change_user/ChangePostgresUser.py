from rest.user.operation.core import IPostgresUser
from ..excepton import UserNotFoundError
from ..excepton import PostgresMethodError
from rest.models import ResponseDTO
from ..postgres import Users

__all__ = [
    "ChangePostgresUser"
]


class ChangePostgresUser(IPostgresUser):
    def work(self) -> ResponseDTO:
        try:
            user = self.session.query(Users).filter(Users.uuid == self.request.body.user.uuid).one()
            user.full_name = self.request.body.user.full_name
        except Exception:
            raise UserNotFoundError(f"User with uuid {self.request.body.user.uuid} not found in database")
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        return ResponseDTO(
            status_code=204
        )
