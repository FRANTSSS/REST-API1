import os

from dotenv import load_dotenv

from ioc_container import ioc
from models import EnvDTO
from service import IService
from service import PostgresFactory
from service import RedisFactory
from service import UserService

__all__ = [
    "bootstrap"
]


def bootstrap():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    env = EnvDTO(
        storage_type=os.environ["STORAGE_TYPE"],
        database_user=os.environ["DATABASE_USER"],
        database_password=os.environ["DATABASE_PASSWORD"],
        database_host=os.environ["DATABASE_HOST"],
        database_port=os.environ["DATABASE_PORT"],
        database_name=os.environ["DATABASE_NAME"]
    )
    if env.storage_type == "redis":
        factory = RedisFactory()
    elif env.storage_type == "postgres":
        factory = PostgresFactory(env)
    user_service = UserService(factory)
    ioc.set_instance(IService, user_service)

# the call is needed solely to execute the Bootstrap before connecting
# the Routes and receiving data from the container
bootstrap()
