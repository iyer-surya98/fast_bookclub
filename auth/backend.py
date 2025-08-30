from fastapi_users.authentication import BearerTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend
from dotenv import get_key

bearer_transport = BearerTransport(
    token_url = "auth/jwt/login"
)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=get_key("SECRET"),
        lifetime_seconds=get_key("JWT_LIFETIME_SECONDS")
    )

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)