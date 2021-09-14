from .Storage import Storage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.users import Users, DeclarativeBase


#конкретный класс Storage с использованием postgresql
class StoragePostgre(Storage):
    def __init__(self):
        super().__init__()
        str_connect = f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        engine = create_engine(str_connect)
        DeclarativeBase.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

#добавление юзера
    def add_user(self, fio: str) -> str:
        session = self.Session()
        user = Users(FIO=fio)
        session.add(user)
        session.commit()
        return "OK"

#получение юзера по id
    def get_user(self, ID: int) -> Users:
        session = self.Session()
        try:
            user_by_id = session.query(Users).filter(Users.id == ID).one()
            return user_by_id
        except:
            raise ValueError(ID)

#удаление юзера
    def del_user(self, id_from_delete: int) -> str:
        session = self.Session()
        try:
            i = session.query(Users).filter(Users.id == id_from_delete).one()
            session.delete(i)
            session.commit()
            return "OK"
        except:
            raise ValueError(id_from_delete)

#изменение данных юзера по id
    def change_user(self, ID: int, fio: str) -> str:
        session = self.Session()
        try:
            i = session.query(Users).filter(Users.id == ID).one()
            i.FIO = fio
            session.add(i)
            session.commit()
            return "OK"
        except:
            raise ValueError(ID, fio)