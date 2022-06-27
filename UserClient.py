from ioc_container import ioc
from models import EnvDTO
from models import User
from user.impl.postgres import PostgresFactory
from user.impl.redis import RedisFactory

__all__ = [
    "UserClient"
]


class UserClient:
    def __init__(self):
        env = ioc.get_instance(EnvDTO)
        if env.storage_type == "redis":
            self.__factory = RedisFactory()
        elif env.storage_type == "postgres":
            self.__factory = PostgresFactory(env)

    def add_user(self, full_name: str) -> User:
        method = self.__factory.get_method("add")
        user = method.work(full_name=full_name)
        return user

    def get_user(self, uuid: str) -> User:
        method = self.__factory.get_method("get")
        user = method.work(uuid)
        return user

    def change_user(self, uuid: str, new_full_name: str) -> User:
        method = self.__factory.get_method("change")
        user = method.work(uuid, new_full_name)
        return user

    def delete_user(self, uuid) -> User:
        method = self.__factory.get_method("delete")
        user = method.work(uuid)
        return user
