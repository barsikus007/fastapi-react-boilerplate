from os import getenv

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar


Select.inherit_cache = True
SelectOfScalar.inherit_cache = True

DATABASE_URL = getenv('DATABASE_URL')
engine = create_async_engine(DATABASE_URL, echo=bool(getenv('DEBUG')), future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
