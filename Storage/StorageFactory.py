from .Storage import Storage
from .StoragePostgre import StoragePostgre
from .StorageRedis import StorageRedis


#класс фабрики
class StorageFactory:
    def get_type_db(self, type_db: str) -> Storage:
        if type_db.lower().strip() == "postgresql":
            return StoragePostgre()
        elif type_db.lower().strip() == "redis":
            return StorageRedis()
        else:
            raise ValueError(type_db)