from .models.RequestDTO import RequestDTO
from .models.ResponseDTO import ResponseDTO
from .user import UserStrategy


__all__ = [
    "APIClient"
]


# An api client is needed to encapsulate the strategy and
# to be able to add operations with other objects
class APIClient:
    @staticmethod
    def work_method(request: RequestDTO) -> ResponseDTO:
        response = ResponseDTO(
            status_code=422)
        if "user" in request.url:
            response = UserStrategy.get_method(request)
        return response
