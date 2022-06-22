from ..models import ResponseDTO
from ..models import RequestDTO
from .operation import AbstractFactory


__all__ = [
    "UserStrategy"
]


# AbstractFactory is used as a selector that returns factory objects
class UserStrategy:
    @staticmethod
    def get_method(request: RequestDTO) -> ResponseDTO:
        factory = AbstractFactory.get_factory(request)
        response = factory.get_operation()
        return response
