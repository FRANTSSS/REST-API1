from user.core import IRedisMethod
from .AddRedisUser import AddRedisUser
from .ChangeRedisUser import ChangeRedisUser
from .DeleteRedisUser import DeleteRedisUser
from .GetRedisUser import GetRedisUser

__all__ = [
    "RedisFactory"
]


class Selector:
    @staticmethod
    def get_action(action_name: str) -> IRedisMethod:
        action_dict = {
            "add": AddRedisUser,
            "get": GetRedisUser,
            "change": ChangeRedisUser,
            "delete": DeleteRedisUser
        }
        return action_dict[action_name]


class RedisFactory:
    def __init__(self):
        pass

    def get_method(self, method_name: str):
        method = Selector.get_action(method_name)
        return method
