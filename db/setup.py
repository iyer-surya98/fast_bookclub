import motor.motor_asyncio
from beanie import Document
from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from dotenv import get_key

client = motor.motor_asyncio.AsyncIOMotorClient(
    host=get_key("DATABASE_URL"), 
    uuidRepresentation="standard"
)

db = client[get_key("DATABASE_NAME")]

class User(BeanieBaseUser, Document):
    username: str
    display_name: str
    favourites: list[PydanticObjectId]
    reviews: list[PydanticObjectId]

async def get_user_db():
    yield BeanieUserDatabase(User)