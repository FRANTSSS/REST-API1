from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import EnvDTO
from .PostgresUserRepository import PostgresUserRepository
from .Users import DeclarativeBase
from .exception import PostgresMethodError

__all__ = [
    "PostgresFactory"
]


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

    def get_user_repository(self):
        repos = PostgresUserRepository(self.session)
        return repos
