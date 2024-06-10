from uuid import UUID

from fastapi import Request, Response, Depends
from fastapi_users import BaseUserManager, UUIDIDMixin

from src.auth.models import User, get_user_db


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):

    reset_password_token_secret = "SECRET"
    verification_token_secret = "SECRET"

    async def on_after_register(
        self, user: User, request: Request | None = None
    ) -> None:
        return await super().on_after_register(user, request)

    async def on_after_login(
        self,
        user: User,
        request: Request | None = None,
        response: Response | None = None,
    ) -> None:
        return await super().on_after_login(user, request, response)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


