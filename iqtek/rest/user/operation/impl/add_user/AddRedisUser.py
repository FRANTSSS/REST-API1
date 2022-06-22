from uuid import uuid4
import redis
from rest.user.operation.core.IRedisUser import IRedisUser
from rest.models import ResponseDTO
from ..excepton import RedisMethodError

__all__ = [
    "AddRedisUser"
]


class AddRedisUser(IRedisUser):
    def work(self) -> ResponseDTO:
        uuid = uuid4()
        r = redis.Redis()
        if not r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if r.mset({str(uuid): self.request.body.user.full_name}):
            self.request.body.user.uuid = uuid
        else:
            raise RedisMethodError("Redis method mset is failed")

        return ResponseDTO(
            status_code=201,
            body=self.request.body
        )
