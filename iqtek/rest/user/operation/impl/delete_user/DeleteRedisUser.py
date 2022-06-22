import redis
from rest.user.operation.core.IRedisUser import IRedisUser
from rest.models import ResponseDTO
from ..excepton import RedisMethodError

__all__ = [
    "DeleteRedisUser"
]


class DeleteRedisUser(IRedisUser):
    def work(self) -> ResponseDTO:
        uuid = self.request.url.split("/")[2]
        r = redis.Redis()
        if not r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if r.get(uuid):
            r.delete(uuid)
        else:
            raise RedisMethodError("Redis method delete is failed")
        return ResponseDTO(
            status_code=204
        )
