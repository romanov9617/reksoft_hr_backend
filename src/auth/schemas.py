import uuid
from typing import Optional, List

from pydantic import Field
from fastapi_users import schemas

from src.enums import UserRole


class UserBase(schemas.BaseUser[uuid.UUID]):

    role: UserRole


class UserRead(UserBase):

    pass


class UserCreate(schemas.BaseUserCreate):

    pass


class UserUpdate(schemas.BaseUserUpdate):

    pass
