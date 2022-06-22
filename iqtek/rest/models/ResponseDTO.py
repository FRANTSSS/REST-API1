from pydantic import BaseModel
from .User import User


class ResponseDTO(BaseModel):
    status_code: int
    body: User = None
