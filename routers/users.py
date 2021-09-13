from shemas.users import UserCreate
from settings import get_env
from db import *
from fastapi import APIRouter

router = APIRouter()
get_env()#добавление переменных окружения из файла .env

db = DbUser()#класс для работы с бд(postgresql) или redis
db.engine_create()#подключение к бд

#получение юзера по id
@router.get("/getUser")
def get_usr(id: int):
	return {"message": db.get_user(id)}

#добавление юзера
@router.post("/addUser")
def add_usr(fio: UserCreate):
	return {"message": db.add_user(fio.fio)}

#изменение данных юзера по id
@router.put("/changeUser")
def change_usr(id: int, fio: str):
	return {"message": db.change_user(id, fio)}

#удаление юзера
@router.delete("/deleteUser")
def del_usr(id: int):
	return {"message": db.del_user(id)}