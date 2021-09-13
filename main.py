import uvicorn
from fastapi import FastAPI
from routers.users import router
#создание приложения
app = FastAPI()
#подключение роутов
app.include_router(router)

if __name__ == "__main__":
	#запуск на локальном хосте
	uvicorn.run(app,
				host="0.0.0.0",
				port=8000)
