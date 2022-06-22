from rest.user.exception import UserMethodError


__all__ = [
    "UserNotFoundError",
    "RedisMethodError",
    "PostgresMethodError"
]


class UserNotFoundError(UserMethodError):
    pass


class RedisMethodError(UserMethodError):
    pass


class PostgresMethodError(UserMethodError):
    pass
