import redis
from rest.user.operation.core.IRedisUser import IRedisUser
from rest.models import ResponseDTO
from ..excepton import RedisMethodError

__all__ = [

]


class ChangeRedisUser(IRedisUser):
    def work(self) -> ResponseDTO:
        r = redis.Redis()
        if not r.ping():
            raise RedisMethodError("Redis is failed: No access to Redis")
        if r.get(self.request.body.user.uuid):
            r[self.request.body.user.uuid] = self.request.body.user.full_name
        else:
            raise RedisMethodError("Redis method change is failed")
        return ResponseDTO(
            status_code=204
        )
