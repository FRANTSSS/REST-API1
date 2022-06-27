from uuid import uuid4

import redis

from models import User
from repository.exception import RedisMethodError
from repository.exception import UserNotFoundError
from .IUserRepository import IUserRepository

__all__ = [
    "RedisUserRepository"
]


class RedisUserRepository(IUserRepository):
    def __init__(self, r: redis.Redis):
        self.r = r

    def add(self, full_name: str) -> User:
        uuid = str(uuid4())
        if not self.r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if self.r.mset({str(uuid): full_name}):
            return User(uuid, full_name)
        else:
            raise RedisMethodError("Redis method mset is failed")

    def get(self, uuid: str) -> User:
        try:
            full_name = self.r.get(uuid)
        except Exception as e:
            raise RedisMethodError(f"Redis method is failed: {e}")
        if full_name is not None:
            return User(uuid, full_name)
        else:
            raise UserNotFoundError(f"User with uuid {uuid} not found in storage")

    def update(self, uuid: str, full_name):
        if not self.r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if self.r.get(uuid):
            self.r[uuid] = full_name
        else:
            raise UserNotFoundError(f"User with uuid {uuid} not found in storage")

    def delete(self, uuid: str):
        if not self.r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if self.r.get(uuid):
            self.r.delete(uuid)
        else:
            raise UserNotFoundError(f"User with uuid {uuid} not found in storage")
