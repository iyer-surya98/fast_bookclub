from fastapi_users.authentication import BearerTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend
from dotenv import get_key, find_dotenv

dotenv_path = find_dotenv()

bearer_transport = BearerTransport(
    tokenUrl = "auth/jwt/login"
)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=get_key(
            dotenv_path=dotenv_path,
            key_to_get="SECRET"),
        lifetime_seconds=int(get_key(
            dotenv_path=dotenv_path,
            key_to_get="JWT_LIFETIME_SECONDS"))
    )

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)