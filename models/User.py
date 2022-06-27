
__all__ = [
    "User"
]


class User:
    def __init__(self, uuid: str = None, full_name: str = None):
        self.__uuid = uuid
        self.__full_name = full_name

    @property
    def uuid(self):
        return self.__uuid

    @property
    def full_name(self):
        return self.__full_name
