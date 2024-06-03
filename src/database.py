import uuid
from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


from src.config import settings


engine = create_async_engine(settings.DB_PROD_URL)

session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session


class Base(DeclarativeBase):

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
