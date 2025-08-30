import motor.motor_asyncio
from beanie import Document
from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from dotenv import find_dotenv, get_key
from typing import List
from pydantic import Field

dotenv_path = find_dotenv()
client = motor.motor_asyncio.AsyncIOMotorClient(
    host=get_key(
        dotenv_path=dotenv_path,
        key_to_get="DATABASE_URL"
    ), 
    uuidRepresentation="standard"
)

db = client[get_key(dotenv_path=dotenv_path,key_to_get="DATABASE_NAME")]

class User(BeanieBaseUser, Document):
    username: str
    display_name: str
    favourites: List[PydanticObjectId] = Field(default_factory=list)
    reviews: List[PydanticObjectId] = Field(default_factory=list)

async def get_user_db():
    yield BeanieUserDatabase(User)