from abc import ABC
from abc import abstractmethod
from rest.models import RequestDTO
from rest.models import ResponseDTO

__all__ = [
    "IRedisUser"
]


class IRedisUser(ABC):
    def __init__(self, request: RequestDTO):
        self.request = request

    @abstractmethod
    def work(self) -> ResponseDTO:
        raise NotImplementedError
