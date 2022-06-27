from models import User

__all__ = [
    "IUserRepository"
]


class IUserRepository:
    def add(self, full_name: str) -> User:
        raise NotImplementedError

    def get(self, uuid: str) -> User:
        raise NotImplementedError

    def update(self, uuid: str, full_name):
        raise NotImplementedError

    def delete(self, uuid: str):
        raise NotImplementedError
