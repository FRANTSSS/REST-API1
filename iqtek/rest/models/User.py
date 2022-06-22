from pydantic import BaseModel

__all__ = [
    "User",
    "DataUser"
]


class DataUser(BaseModel):
    uuid: str = None
    full_name: str = None


class User(BaseModel):
    user: DataUser
