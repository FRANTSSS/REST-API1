from shemas import UserCreate
from settings import get_env
from Storage.StorageCreator import StorageCreator
from fastapi import APIRouter

router = APIRouter()
get_env()#добавление переменных окружения из файла .env

storage_create = StorageCreator()
storage = storage_create.create_object()

#получение юзера по id
@router.get("/getUser")
def get_usr(id: int) -> dict:
	try:
		return {"message": storage.get_user(id)}
	except ValueError:
		return {"message": "InputDataError"}

#добавление юзера
@router.post("/addUser")
def add_usr(fio: UserCreate) -> dict:
	return {"message": storage.add_user(fio.fio)}


#изменение данных юзера по id
@router.put("/changeUser")
def change_usr(id: int, fio: str) -> dict:
	try:
		return {"message": storage.change_user(id, fio)}
	except ValueError:
		return {"message": "InputDataError"}
	except "NotFoundError":
		return {"message": "NotFoundError"}


#удаление юзера
@router.delete("/deleteUser")
def del_usr(id: int) -> dict:
	try:
		return {"message": storage.del_user(id)}
	except:
		return {"message": "InputDataError"}