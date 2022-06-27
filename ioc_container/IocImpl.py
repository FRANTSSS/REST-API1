from typing import MutableMapping
from typing import Type
from typing import TypeVar

from .Ioc import Ioc
from .exception import IocNotFoundInstance

__all__ = [
    "IocImpl"
]


T = TypeVar('T')


class IocImpl(Ioc):
    def __init__(self):
        self.__instances: MutableMapping[Type[T], T] = {}

    def get_instance(self, key: Type[T]) -> T:
        try:
            return self.__instances[key]
        except KeyError:
            raise IocNotFoundInstance(f"Instance with key {key} not found")

    def set_instance(self, key: Type[T], instance: T):
        self.__instances[key] = instance
