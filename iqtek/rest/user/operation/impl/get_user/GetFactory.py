import os
from .GetPostgresUser import GetPostgresUser
from .GetRedisUser import GetRedisUser
from rest.user.operation.core import IFactory
from rest.models import ResponseDTO

__all__ = [
    "GetFactory"
]


class GetFactory(IFactory):
    def get_operation(self) -> ResponseDTO:
        if os.environ["STORAGE_TYPE"].strip().lower() == "redis":
            method = GetRedisUser(self.request)
            response = method.work()
            return response
        elif os.environ["STORAGE_TYPE"].strip().lower() == "postgres":
            method = GetPostgresUser(self.request, self.session)
            response = method.work()
            return response
