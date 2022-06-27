from abc import ABC
from abc import abstractmethod
from typing import Type
from typing import TypeVar

__all__ = [
    "Ioc"
]


T = TypeVar('T')


class Ioc(ABC):
    @abstractmethod
    def get_instance(self, key: Type[T]) -> T:
        raise NotImplementedError()

    @abstractmethod
    def set_instance(self, key: Type[T], instance: T) -> None:
        raise NotImplementedError()
