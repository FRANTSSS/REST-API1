from .Storage import Storage
import redis


#работа с postgre осуществляется через sqlalchemy
#функция замыкания для определения последнего id в redis
def append_id(n: int):
    def step():
        nonlocal n
        r = n
        n += 1
        return str(r)
    return step

#конкретный класс Storage с использованием redis
class StorageRedis(Storage):
    def __init__(self):
        super().__init__()
        self.r = redis.Redis()
        try:
            list_id = [int(i.decode("utf-8")) for i in self.r.keys()]
            my_id = str(max(list_id))
            self.ID = append_id(int(my_id))
            self.ID()
        except:
            my_id = "1"
            self.ID = append_id(int(my_id))

#добавление юзера
    def add_user(self, fio: str) -> str:
        self.r.mset({self.ID(): fio})
        return "OK"

#получение юзера по id
    def get_user(self, ID: int) -> dict:
        try:
            return {ID: self.r.get(ID).decode('utf-8')}
        except:
            raise ValueError(ID)

#удаление юзера
    def del_user(self, id_from_delete: int) -> str:
        try:
            if self.r.get(id_from_delete) is None:
                raise "NotFoundError"
            self.r.delete(id_from_delete)
            return "OK"
        except:
            raise ValueError(id_from_delete)

#изменение данных юзера по id
    def change_user(self, ID: int, fio: str) -> str:
        try:
            if self.r.get(ID) is None:
                raise "NotFoundError"
            self.r[ID] = fio
            return "OK"
        except:
            raise ValueError(ID, fio)