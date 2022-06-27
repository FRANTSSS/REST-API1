from abc import ABC
from abc import abstractmethod

from models import User

__all__ = [
    "IService"
]


class IService(ABC):
    @abstractmethod
    def add_user(self, full_name: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, uuid: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, uuid: str, new_full_name: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, uuid) -> User:
        raise NotImplementedError
