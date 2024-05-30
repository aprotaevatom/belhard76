from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Optional, Any

from pydantic import BaseModel, PositiveInt, Field
from pydantic.alias_generators import to_snake
from sqlalchemy import (
    Column,
    SMALLINT,
    VARCHAR,
    ForeignKey,
    INT,
    BIGINT,
    TIMESTAMP,
    create_engine,
    BOOLEAN,
    insert,
    update,
    delete,
    select,
    and_,
    or_,
    any_,
    all_,
    func, label, CheckConstraint, TypeDecorator, Dialect
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    sessionmaker,
    Session,
    selectinload,
    joinedload,
    with_loader_criteria, aliased, declared_attr
)
from sqlalchemy.sql.type_api import _T

POSTGRES_DSN = "postgresql://admin:password@0.0.0.0:5432/bh"
engine = create_engine(url=POSTGRES_DSN)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return f"{to_snake(camel=cls.__name__)}s"
    pass


class FileSystemStorage(TypeDecorator):
    impl = VARCHAR
    cache_ok = True

    def __init__(self, upload_to: str | Path = None, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        if isinstance(upload_to, str):
            upload_to = Path(upload_to)

        upload_to.mkdir(mode=0o777, exist_ok=True)
        if not upload_to.is_dir():
            raise ValueError

        self.upload_to = upload_to

    def process_bind_param(self, value: BytesIO, dialect: Dialect) -> Optional[str]:
        if value is None:
            return None

        if not isinstance(value, BytesIO):
            raise TypeError

        filename = getattr(value, "name")
        if filename is None:
            raise ValueError

        value.seek(0)
        with self.upload_to.joinpath(filename).open(mode="wb") as file:
            file.write(value.read())

        return filename

    def process_result_value(self, value: str, dialect: Dialect) -> Optional[BytesIO]:
        if value is None:
            return None

        with self.upload_to.joinpath(value).open("rb") as file:
            b = BytesIO(initial_bytes=file.read())
            b.name = value
        return b


class NewsTag(Base):
    __tablename__ = "news_tags"

    news_id = Column(
        BIGINT,
        ForeignKey(column="news.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True
    )
    tag_id = Column(
        BIGINT,
        ForeignKey(column="tags.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True
    )


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = (
        CheckConstraint(sqltext="length(name) >= 5"),
    )

    id = Column(SMALLINT, primary_key=True)
    _name = Column("name", VARCHAR(length=32), nullable=False, unique=True)

    news = relationship(
        argument="News",
        back_populates="category",
        uselist=True
    )

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) < 5:
            raise ValueError("length of category name must be great equal 5")

    def __str__(self) -> str:
        return self.name


class Tag(Base):
    __tablename__ = "tags"

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32), nullable=False, unique=True)

    news = relationship(
        argument="News",
        secondary=NewsTag.__table__,
        back_populates="tags",
        uselist=True
    )

    def __str__(self) -> str:
        return self.name


class News(Base):
    __tablename__ = "news"

    id = Column(BIGINT, primary_key=True)
    title = Column(VARCHAR(length=128), nullable=False)
    content = Column(VARCHAR, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now, nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=datetime.now, nullable=True)
    category_id = Column(
        SMALLINT,
        ForeignKey(
            column="categories.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=False
    )
    is_published = Column(BOOLEAN, default=False, nullable=False)
    image = Column(FileSystemStorage(upload_to="./photo"))

    category = relationship(
        argument=Category,
        back_populates="news",
        uselist=False,
    )
    tags = relationship(
        argument=Tag,
        secondary=NewsTag.__table__,
        back_populates="news",
        uselist=True,
    )


# with session_maker() as session:  # type: Session
    # cat1 = Category(name="Sport")
    # cat2 = Category(name="Finance")
    # session.add_all(instances=[cat1, cat2])
    # try:
    #     session.commit()
    # except IntegrityError:
    #     pass
    # session.refresh(instance=cat1)
    # session.refresh(instance=cat2)
    # stmt = insert(table=Category).values(
    #     [
    #         {
    #             "name": "Politic"
    #         },
    #         {
    #             "name": "Art"
    #         }
    #     ]
    # )
    # session.execute(statement=stmt)
    # session.commit()
    # session.add(instance=Category(name="Music"))
    # session.commit()
    # cat = session.get(entity=Category, ident=2)
    # cat.name = "Финансы"
    # session.commit()
    # stmt = update(table=Category).values(name="Спорт").filter_by(id=1)
    # session.execute(statement=stmt)
    # session.commit()
    # cat = session.get(entity=Category, ident=3)
    # session.delete(instance=cat)
    # session.commit()
    # stmt = delete(Category).filter_by(id=4)
    # session.execute(statement=stmt)
    # session.commit()
    # cat = session.get(entity=Category, ident=1)
    # news = News(title="Новость 1", content="BOOOOOOOODY")
    # cat.news.append(news)
    # session.commit()
    # news = session.get(entity=News, ident=1)
    # news.is_published = True
    # session.commit()
    # statement = select(Category, func.count(News.id).label("news_count")).join(News, onclause=Category.id == News.category_id).group_by(Category.id)
    # response = session.execute(statement)
    # print(response.mappings().all())


class NewsDTO(BaseModel):
    id: PositiveInt
    title: str = Field(max_length=128)
    content: str
    is_published: bool
    created_at: datetime
    updated_at: datetime


class CategoryDTO(BaseModel):
    id: PositiveInt
    name: str = Field(max_length=32)
    news: list[NewsDTO]


# with session_maker() as session:
#     cat = session.get(entity=Category, ident=1, options=[joinedload(Category.news)])
#     dto = CategoryDTO.model_validate(obj=cat, from_attributes=True)
#     print(dto)


with (
    session_maker() as session,
    # open("binance.png", "rb") as file
):
    o = session.get(entity=News, ident=2)
    print(o.image.read())
    # f = BytesIO(initial_bytes=file.read())
    # f.name = file.name
    # n = News(title="Binance", content="Binance", category_id=1, image=f)
    # session.add(n)
    # session.commit()
    # session.refresh(n)
    # print(n.image)
