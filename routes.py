from fastapi import APIRouter
from user.exception import UserNotFoundError


__all__ = [
    "route"
]


route = APIRouter()


@route.post("/users")
def add_user(full_name: str):
    user = user_client.add_user(full_name)
    return {"status": "success", "body": {"uuid": user.uuid, "full_name": user.full_name, "status": "working"}}


@route.get("/users/{uuid}")
def get_user(uuid: str):
    try:
        user = user_client.get_user(uuid)
        return {"status": "success", "body": {"uuid": user.uuid, "full_name": user.full_name, "status": "working"}}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}


@route.put("/users")
def change_user(uuid: str, new_full_name: str):
    try:
        user = user_client.put_user(uuid, new_full_name)
        return {"status": "success", "body": {"uuid": user.uuid, "new_full_name": user.full_name, "status": "working"}}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}


@route.delete("/users/{uuid}")
def delete_user(uuid: str):
    try:
        user = user_client.delete_user(uuid)
        return {"status": "success", "body": {"uuid": user.uuid, "new_full_name": user.full_name, "status": "deleted"}}
    except UserNotFoundError as e:
        return {"status": "failed", "body": {"err": f"User with uuid {uuid} not found"}}
