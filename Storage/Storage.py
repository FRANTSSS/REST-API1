import os


#родительский класс
class Storage:
    def __init__(self):
        #переменные окружения
        self.DB_TYPE = os.environ.get("DB_TYPE")#тип хранения данных, при выборе типа "redis" остальные данные не используются
        self.DB_USER = os.environ.get("DB_USER")#юзер
        self.DB_PASS = os.environ.get("DB_PASS")#пароль
        self.DB_HOST = os.environ.get("DB_HOST")#хост
        self.DB_NAME = os.environ.get("DB_NAME")#имя бд
        self.DB_PORT = os.environ.get("DB_PORT")#порт