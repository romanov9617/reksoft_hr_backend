from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class NewsBase(BaseModel):

    title: str
    description: str
    content: str

    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    pass


class NewsRead(NewsBase):
    id: UUID


class NewsUpdate(NewsBase):
    pass


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id: UUID
    news: list[NewsRead]


class TagUpdate(TagBase):
    pass
