import os
from ioc_container import ioc
from models import EnvDTO

__all__ = [
    "bootstrap"
]


def bootstrap():
    env = EnvDTO(
        storage_type=os.environ["STORAGE_TYPE"],
        database_user=os.environ["DATABASE_USER"],
        database_password=os.environ["DATABASE_PASSWORD"],
        database_host=os.environ["DATABASE_HOST"],
        database_port=os.environ["DATABASE_PORT"],
        database_name=os.environ["DATABASE_NAME"]
    )
    ioc.set_instance(EnvDTO, env)
