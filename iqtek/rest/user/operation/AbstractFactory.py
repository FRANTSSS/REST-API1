import os
from rest.user.exception import AbstractFactoryMethodError
from rest.user.exception import EnvNotFoundError
from rest.models import RequestDTO
from rest.user.operation.core import IFactory
from .impl import ChangeFactory
from .impl import AddFactory
from .impl import GetFactory
from .impl import DeleteFactory
from .impl import get_postgres_session


__all__ = [
    "AbstractFactory"
]


# Each factory implements its own method for working with storage objects
class AbstractFactory:
    @staticmethod
    def get_factory(request: RequestDTO) -> IFactory:
        if os.environ["STORAGE_TYPE"].strip().lower() not in ("postgres", "redis"):
            raise EnvNotFoundError(f"Storage type {os.environ['STORAGE_TYPE']} is not defined")
        session = get_postgres_session()

        if request.method == "get" and "/user/" in request.url:
            factory = GetFactory(request, session)
        elif request.method == "post" and request.url in ("/user/", "/user"):
            factory = AddFactory(request, session)
        elif request.method == "put" and request.url in ("/user/", "/user"):
            factory = ChangeFactory(request, session)
        elif request.method == "delete" and "/user/" in request.url:
            factory = DeleteFactory(request, session)
        else:
            raise AbstractFactoryMethodError(f"method {request.url} is not defined")
        return factory
