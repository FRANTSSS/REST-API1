from abc import ABC
from abc import abstractmethod
from sqlalchemy.orm import sessionmaker
from rest.models import RequestDTO
from rest.models import ResponseDTO

__all__ = [
    "IPostgresUser"
]


class IPostgresUser(ABC):
    def __init__(self, request: RequestDTO, session: sessionmaker):
        self.session = session()
        self.request = request

    @abstractmethod
    def work(self) -> ResponseDTO:
        raise NotImplementedError
