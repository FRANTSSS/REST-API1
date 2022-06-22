from fastapi import APIRouter
from fastapi import Body
from fastapi import Response
from .APIClient import APIClient
from .example import *
from .models import User
from .models import DataUser
from .models import RequestDTO


__all__ = [
    "route"
]


route = APIRouter()


@route.post("/user/", response_model=dict, responses=add_user_response)
def add_user(api_response: Response,
             user: User = Body(examples=add_user_example)) -> User:
    request = RequestDTO(
        url="/user",
        method="post",
        body=user
    )
    response = APIClient.work_method(request)
    api_response.status_code = response.status_code
    return response.body


@route.get("/user/{uuid}", response_model=dict, responses=get_user_response)
def get_user(api_response: Response, uuid: str) -> User:
    request = RequestDTO(
        url=f"/user/{uuid}",
        method="get",
        body=User(
            user=DataUser()
        )
    )
    response = APIClient.work_method(request)
    api_response.status_code = response.status_code
    return response.body


@route.put("/user/", responses=change_user_response)
def change_user(api_response: Response,
                user: User = Body(examples=change_user_example)) -> None:
    request = RequestDTO(
        url="/user/",
        method="put",
        body=user
    )
    response = APIClient.work_method(request)
    api_response.status_code = response.status_code


@route.delete("/user/{uuid}", responses=delete_user_response)
def delete_user(api_response: Response, uuid: str) -> None:
    request = RequestDTO(
        url=f"/user/{uuid}",
        method="delete",
        body=User(
            user=DataUser()
        )
    )
    response = APIClient.work_method(request)
    api_response.status_code = response.status_code
