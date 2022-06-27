
__all__ = [
    "UserNotFoundError",
    "PostgresMethodError",
    "RedisMethodError"
]


class UserNotFoundError(Exception):
    pass


class PostgresMethodError(Exception):
    pass


class RedisMethodError(Exception):
    pass
