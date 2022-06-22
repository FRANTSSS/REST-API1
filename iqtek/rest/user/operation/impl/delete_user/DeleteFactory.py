import os
from .DeletePostgresUser import DeletePostgresUser
from .DeleteRedisUser import DeleteRedisUser
from rest.user.operation.core import IFactory
from rest.models import ResponseDTO

__all__ = [
    "DeleteFactory"
]


class DeleteFactory(IFactory):
    def get_operation(self) -> ResponseDTO:
        if os.environ["STORAGE_TYPE"].strip().lower() == "redis":
            method = DeleteRedisUser(self.request)
            response = method.work()
            return response
        elif os.environ["STORAGE_TYPE"].strip().lower() == "postgres":
            method = DeletePostgresUser(self.request, self.session)
            response = method.work()
            return response
