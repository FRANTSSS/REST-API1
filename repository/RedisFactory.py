import redis

from .IUserRepository import IUserRepository
from .RedisUserRepository import RedisUserRepository

__all__ = [
    "RedisFactory"
]


class RedisFactory:
    def __init__(self):
        self.r = redis.Redis()

    def get_user_repository(self) -> IUserRepository:
        repos = RedisUserRepository(self.r)
        return repos
