import os
from .ChangePostgresUser import ChangePostgresUser
from .ChangeRedisUser import ChangeRedisUser
from rest.user.operation.core import IFactory
from rest.models import ResponseDTO

__all__ = [
    "ChangeFactory"
]


class ChangeFactory(IFactory):
    def get_operation(self) -> ResponseDTO:
        if os.environ["STORAGE_TYPE"].strip().lower() == "redis":
            method = ChangeRedisUser(self.request)
            response = method.work()
            return response
        elif os.environ["STORAGE_TYPE"].strip().lower() == "postgres":
            method = ChangePostgresUser(self.request, self.session)
            response = method.work()
            return response
