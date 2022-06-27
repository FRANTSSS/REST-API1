from models import User
from .IService import IService

__all__ = [
    "UserService"
]


class UserService(IService):
    def __init__(self, user_factory):
        self.__repos = user_factory.get_user_repository()

    def add_user(self, full_name: str) -> User:
        user = self.__repos.add(full_name)
        return user

    def get_user(self, uuid: str) -> User:
        user = self.__repos.get(uuid)
        return user

    def update_user(self, uuid: str, new_full_name: str):
        user = self.__repos.update(uuid, new_full_name)

    def delete_user(self, uuid):
        user = self.__repos.delete(uuid)
