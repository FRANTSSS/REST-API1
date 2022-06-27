from pydantic import BaseModel

__all__ = [
    "EnvDTO"
]


class EnvDTO(BaseModel):
    storage_type: str
    database_user: str = None
    database_password: str = None
    database_host: str = None
    database_port: str = None
    database_name: str = None
