from rest.user.operation.core import IPostgresUser
from ..excepton import UserNotFoundError
from ..excepton import PostgresMethodError
from rest.models import ResponseDTO
from ..postgres import Users

__all__ = [
    "DeletePostgresUser"
]


class DeletePostgresUser(IPostgresUser):
    def work(self) -> ResponseDTO:
        uuid = self.request.url.split("/")[2]
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        try:
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        return ResponseDTO(
            status_code=204
        )
