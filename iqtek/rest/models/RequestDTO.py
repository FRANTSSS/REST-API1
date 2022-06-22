from pydantic import BaseModel
from .User import User


class RequestDTO(BaseModel):
    url: str
    method: str
    body: User
