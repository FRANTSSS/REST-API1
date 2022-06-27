from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from AddPostgresUser import AddPostgresUser
from ChangePostgresUser import ChangePostgresUser
from DeletePostgresUser import DeletePostgresUser
from GetPostgresUser import GetPostgresUser
from models import EnvDTO
from user.core import IPostgresMethod
from .Users import DeclarativeBase
from .exception import PostgresMethodError

__all__ = [
    "PostgresFactory"
]


class Selector:
    @staticmethod
    def get_action(action_name: str) -> IPostgresMethod:
        action_dict = {
            "add": AddPostgresUser,
            "get": GetPostgresUser,
            "change": ChangePostgresUser,
            "delete": DeletePostgresUser
        }
        return action_dict[action_name]


class PostgresFactory:
    def __init__(self, env: EnvDTO):
        str_connect = f"postgresql+psycopg2://{env.database_user}:{env.database_password}" \
                      f"@{env.database_host}:" \
                      f"{env.database_port}/{env.database_name}"
        try:
            engine = create_engine(str_connect)
            DeclarativeBase.metadata.create_all(engine)
        except Exception as e:
            raise PostgresMethodError(f"Failed to connect database: {e}")
        self.session = sessionmaker(bind=engine)

    def get_method(self, method_name) -> IPostgresMethod:
        action = Selector.get_action(method_name)
        method = action(self.session)
        return method
