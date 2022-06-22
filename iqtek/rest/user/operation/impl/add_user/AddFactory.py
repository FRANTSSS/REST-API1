import os
from .AddPostgresUser import AddPostgresUser
from .AddRedisUser import AddRedisUser
from rest.user.operation.core import IFactory
from rest.models import ResponseDTO

__all__ = [
    "AddFactory"
]


class AddFactory(IFactory):
    def get_operation(self) -> ResponseDTO:
        if os.environ["STORAGE_TYPE"].strip().lower() == "redis":
            method = AddRedisUser(self.request)
            response = method.work()
            return response
        elif os.environ["STORAGE_TYPE"].strip().lower() == "postgres":
            method = AddPostgresUser(self.request, self.session)
            response = method.work()
            return response
