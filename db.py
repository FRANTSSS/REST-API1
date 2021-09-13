from models.users import Users, DeclarativeBase
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis
#работа с postgre осуществляется через sqlalchemy
#функция замыкания для определения последнего id в redis
def append_id(n):
    def step():
        nonlocal n
        r = n
        n += 1
        return str(r)
    return step

#родительский класс
class DB:
    def __init__(self):
        #переменные окружения
        self.DB_TYPE = os.environ.get("DB_TYPE")#тип хранения данных, при выборе типа "redis" остальные данные не используются
        self.DB_USER = os.environ.get("DB_USER")#юзер
        self.DB_PASS = os.environ.get("DB_PASS")#пароль
        self.DB_HOST = os.environ.get("DB_HOST")#хост
        self.DB_NAME = os.environ.get("DB_NAME")#имя бд
        self.DB_PORT = os.environ.get("DB_PORT")#порт

    def get_type_db(self):#функция определения типа хранения данных
        if self.DB_TYPE.lower().strip() == 'postgresql':#"redis" или "postgresql"
            return True
        else:
            return False


class DbUser(DB):
    #подключение к бд
    def engine_create(self):
        if self.get_type_db():
            str_connect = f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            engine = create_engine(str_connect)
            DeclarativeBase.metadata.create_all(engine)
            self.Session = sessionmaker(bind=engine)
        else:
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
    def add_user(self, fio):
        if self.get_type_db():
            session = self.Session()
            user = Users(FIO=fio)
            session.add(user)
            session.commit()
        else:
            self.r.mset({self.ID(): fio})
        return "OK"

#получение юзера по id
    def get_user(self, ID):
        if self.get_type_db():
            session = self.Session()
            list_users = session.query(Users).all()
            try:
                user_by_id = session.query(Users).filter(Users.id == ID).one()
            except:
                return None
        else:
            try:
                return {ID: self.r.get(ID).decode('utf-8')}
            except:
                return None
        return user_by_id

#удаление юзера
    def del_user(self, id_from_delete):
        if self.get_type_db():
            session = self.Session()
            try:
                i = session.query(Users).filter(Users.id == id_from_delete).one()
                session.delete(i)
                session.commit()
            except:
                return None
        else:
            try:
                if self.r.get(id_from_delete) is None:
                    raise "NotFoundError"
                self.r.delete(id_from_delete)
            except:
                return None
        return "OK"

#изменение данных юзера по id
    def change_user(self, ID, fio):
        if self.get_type_db():
            session = self.Session()
            try:
                i = session.query(Users).filter(Users.id == ID).one()
            except:
                return None
            i.FIO = fio
            session.add(i)
            session.commit()
        else:
            try:
                if self.r.get(ID) is None:
                    raise "NotFoundError"
                self.r[ID] = fio
            except:
                return None
        return "OK"







