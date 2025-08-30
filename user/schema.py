from beanie import PydanticObjectId
from fastapi_users import schemas

class UserRead(schemas.BaseUser[PydanticObjectId]):
    username: str
    display_name: str
    favourites: list[PydanticObjectId]
    reviews: list[PydanticObjectId]

class UserCreate(schemas.BaseUserCreate):
    username: str
    display_name: str

class UserUpdate(schemas.BaseUserUpdate):
    display_name: str