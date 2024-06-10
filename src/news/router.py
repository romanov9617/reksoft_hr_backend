from uuid import UUID

from fastapi import APIRouter, Depends

from src.database import SessionDep
from src.news import models, schemas

router = APIRouter()


@router.get("/", response_model=schemas.NewsRead)
async def get_one_by_id(id_: UUID, session: SessionDep):
    news = await models.News.get_one_by_id(session, id_)
    return news


async def get_all():
    pass


async def get_by_filter():
    pass


async def get_by_tag():
    pass


async def create_news():
    pass


async def update_news():
    pass


async def delete_news():
    pass
