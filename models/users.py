from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

#модель таблицы postgresql
class Users(DeclarativeBase):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    FIO = Column('FIO', String)

    def __repr__(self):
        return f'{{"id": {self.id}, "FIO": {self.FIO}}}'
