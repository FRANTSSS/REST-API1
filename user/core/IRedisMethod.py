from abc import ABC
from abc import abstractmethod

import redis

from models import User

__all__ = [
    "IRedisMethod"
]


class IRedisMethod(ABC):
    def __init__(self):
        self.r = redis.Redis()

    @abstractmethod
    def work(self, uuid=None, full_name=None) -> User:
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self
