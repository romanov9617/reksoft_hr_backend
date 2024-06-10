from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, joinedload

from src.database import Base


class News(Base):

    __tablename__ = "news"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)

    tags: Mapped["Tags"] = relationship(
        back_populates="news", secondary="news_tags", lazy="joined"
    )

    def __repr__(self):
        return f"<News(title={self.title}, description={self.description}, content={self.content})>"


class Tags(Base):

    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(nullable=False)
    news: Mapped["News"] = relationship(
        back_populates="tags",
        secondary="news_tags",
    )

    def __repr__(self):
        return f"<Tags(name={self.name})>"


association_table = Table(
    "association_table",
    Base.metadata,
    Column("news_id", ForeignKey("news.id"), primary_key=True),
    Column("tags_id", ForeignKey("tags.id"), primary_key=True),
)
