import os
from dotenv import load_dotenv

#чтение файла .env и добавление переменных окружения
def get_env():
	dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
	if os.path.exists(dotenv_path):
		load_dotenv(dotenv_path)