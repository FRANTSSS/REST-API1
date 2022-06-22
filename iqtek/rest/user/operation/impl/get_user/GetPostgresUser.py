from rest.user.operation.core import IPostgresUser
from ..excepton import UserNotFoundError
from rest.models import ResponseDTO
from ..postgres import Users

__all__ = [
    "GetPostgresUser"
]


class GetPostgresUser(IPostgresUser):
    def work(self) -> ResponseDTO:
        uuid = self.request.url.split("/")[2]
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).one()
        except Exception as e:
            raise UserNotFoundError(f"User with uuid {uuid} not found in database")
        self.request.body.user.full_name = user[uuid]
        self.request.body.user.uuid = uuid
        return ResponseDTO(
            status_code=200,
            body=self.request.body.user
        )
