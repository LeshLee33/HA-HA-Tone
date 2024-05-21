from fastapi import APIRouter
import pymongo as pm
from pydantic import BaseModel


# Инициализация базы данных MongoDB
client = pm.MongoClient("mongodb://localhost:27017/")
database = client.HAHATone


# Инициализация коллекции с пользователями
users_collection = database.Users


# Инициализация модели записи базы данных
class UserModel(BaseModel):
    _id: str
    username: str
    password: str


# Инициализация роутера
router = APIRouter()


# Инициализация эндпоинта роутера
@router.get("/")
def greetings():
    return """Наш крутой Ха-Ха-Тон"""
