from fastapi import Depends

from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)

from src.database import get_db
from src.auth.models import AccessToken, User


cookie_transport = CookieTransport(cookie_max_age=3600)


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)
