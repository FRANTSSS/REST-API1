import redis
from rest.user.operation.core.IRedisUser import IRedisUser
from ..excepton import UserNotFoundError
from ..excepton import RedisMethodError
from rest.models import ResponseDTO

__all__ = [
    "GetRedisUser"
]


class GetRedisUser(IRedisUser):
    def work(self) -> ResponseDTO:
        r = redis.Redis()
        uuid = self.request.url.split("/")[2]
        try:
            full_name = r.get(uuid)
        except Exception as e:
            raise RedisMethodError(f"Redis method is failed: {e}")
        if full_name is not None:
            self.request.body.user.full_name = full_name
            self.request.body.user.uuid = uuid
            response = ResponseDTO(
                status_code=200,
                body=self.request.body
            )
        else:
            raise UserNotFoundError(f"User with uuid {uuid} not found in storage")
        return response
