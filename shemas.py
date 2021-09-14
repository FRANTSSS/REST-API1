from pydantic import BaseModel

#модель для добавления юзера
class UserCreate(BaseModel):
	fio: str