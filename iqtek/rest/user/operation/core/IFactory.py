from abc import ABC
from abc import abstractmethod
from typing import Optional
from sqlalchemy.orm import sessionmaker
from rest.models import RequestDTO
from rest.models import ResponseDTO

__all__ = [
    "IFactory"
]


class IFactory(ABC):
    def __init__(self, request: RequestDTO, session: Optional[sessionmaker] = None):
        self.request = request
        self.session = session

    @abstractmethod
    def get_operation(self) -> ResponseDTO:
        raise NotImplementedError
