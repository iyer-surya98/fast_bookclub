from fastapi import FastAPI
from contextlib import asynccontextmanager
from beanie import init_beanie
from db.setup import db, User
from user.manager import fastapi_users
from auth.backend import auth_backend
from user.schema import UserCreate, UserRead, UserUpdate

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie(
        database=db,  
        document_models=[
            User,  
        ],
    )
    yield

app = FastAPI(lifespan=lifespan)

# Auth router
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)

# Registration router
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)

# User email verification router
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

# Reset password router
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

# Users router
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get('/')
async def index():
    return {'msg':"Hello world!"}