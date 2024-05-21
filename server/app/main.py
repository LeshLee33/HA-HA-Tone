from fastapi import FastAPI
from uvicorn import run
from database import router


# Инициализация приложения-сервера и добавление всех роутера в него
application = FastAPI()
application.include_router(router)


# Запуск приложения
def start():
    run(app="main:application", reload=True)


if __name__ == "__main__":
    start()
