
__all__ = [
    "UserMethodError",
    "AbstractFactoryMethodError",
    "EnvNotFoundError"
]


class UserMethodError(Exception):
    pass


class AbstractFactoryMethodError(UserMethodError):
    pass


class EnvNotFoundError(UserMethodError):
    pass
