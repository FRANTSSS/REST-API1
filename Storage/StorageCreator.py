from .Storage import Storage
from .StorageFactory import StorageFactory


#класс создания объекта Storage
class StorageCreator(Storage):
    def create_object(self) -> Storage:
        super().__init__()
        db_object = StorageFactory()
        return db_object.get_type_db(self.DB_TYPE)