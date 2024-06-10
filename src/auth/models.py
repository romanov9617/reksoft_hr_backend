from enum import Enum
import uuid

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base, get_db

from src.enums import UserRole


class User(SQLAlchemyBaseUserTableUUID, Base):

    role: Mapped[UserRole] = mapped_column(default=UserRole.SPECIALIST)


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):

    pass


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(
    session: AsyncSession = Depends(get_db),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
