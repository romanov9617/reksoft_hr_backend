from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)
from fastapi_users.authentication import AuthenticationBackend

from src.auth.models import AccessToken, get_access_token_db
from src.auth.transport import cookie_transport
from src.auth.user_manager import get_user_manager


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)

fastapi_users = FastAPIUsers(get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(
    active=True, verified=True, superuser=True
)
