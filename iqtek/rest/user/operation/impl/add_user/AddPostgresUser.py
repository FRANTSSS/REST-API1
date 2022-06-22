from uuid import uuid4
from rest.user.operation.core import IPostgresUser
from ..excepton import PostgresMethodError
from rest.models import ResponseDTO
from ..postgres import Users

__all__ = [
    "AddPostgresUser"
]


class AddPostgresUser(IPostgresUser):
    def work(self) -> ResponseDTO:
        uuid = uuid4()
        user = Users(
            uuid=str(uuid),
            full_name=self.request.body.user.full_name)
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise PostgresMethodError(f"Failed to commit operation in database: {e}")
        self.request.body.user.uuid = uuid
        return ResponseDTO(
            status_code=201,
            body=self.request.body.user
        )
