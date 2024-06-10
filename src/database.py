from datetime import datetime
import uuid
from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy import select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings


engine = create_async_engine(settings.DB_PROD_URL)

session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]


class Base(DeclarativeBase):

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(server_onupdate=func.now(), nullable=True)

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        obj = cls(**kwargs)
        async with session.begin():
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
        return obj

    @classmethod
    async def get_one_by_id(cls, session: AsyncSession, id_: uuid.UUID):
        async with session.begin():
            object = await session.get(cls, id_)
        return object

    @classmethod
    async def get_all(cls, session: AsyncSession):
        async with session.begin():
            objects = await session.execute(select(cls))
        return objects.scalars().all()

    @classmethod
    async def get_by_filter(cls, session: AsyncSession, **kwargs):
        async with session.begin():
            objects = await session.execute(select(cls).filter_by(**kwargs))
        return objects.scalars().all()

    @classmethod
    async def update(cls, session: AsyncSession, id_: uuid.UUID, **kwargs):
        async with session.begin():
            object = await session.get(cls, id_)
            for key, value in kwargs.items():
                setattr(object, key, value)
            await session.commit()
            await session.refresh(object)
        return object

    @classmethod
    async def delete(cls, session: AsyncSession, id_: uuid.UUID):
        async with session.begin():
            object = await session.get(cls, id_)
            await session.delete(object)
            await session.commit()
