from fastapi import APIRouter
from ioc_container import ioc
from service import IService
from service import UserNotFoundError


__all__ = [
    "route"
]


route = APIRouter()
user_service = ioc.get_instance(IService)


@route.post("/users")
def add_user(full_name: str):
    user = user_service.add_user(full_name)
    return {"status": "success", "body": {"uuid": user.uuid, "full_name": user.full_name}}


@route.get("/users/{uuid}")
def get_user(uuid: str):
    try:
        user = user_service.get_user(uuid)
        return {"status": "success", "body": {"uuid": user.uuid, "full_name": user.full_name}}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}


@route.put("/users")
def update_user(uuid: str, new_full_name: str):
    try:
        user = user_service.update_user(uuid, new_full_name)
        return {"status": "success"}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}


@route.delete("/users/{uuid}")
def delete_user(uuid: str):
    try:
        user = user_service.delete_user(uuid)
        return {"status": "success"}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}
