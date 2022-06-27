from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

__all__ = [
    "DeclarativeBase",
    "Users"
]


DeclarativeBase = declarative_base()


class Users(DeclarativeBase):
    __tablename__ = "Users"

    uuid = Column(String, primary_key=True)
    full_name = Column('full_name', String)

    def __repr__(self):
        return f"{{'uuid': {self.uuid}, 'full_name': {self.full_name}}}"
