from abc import ABC
from abc import abstractmethod

from sqlalchemy.orm import sessionmaker

from models import User

__all__ = [
    "IPostgresMethod"
]


class IPostgresMethod(ABC):
    def __init__(self, session: sessionmaker):
        self.session = session()

    @abstractmethod
    def work(self, uuid=None, full_name=None) -> User:
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self
