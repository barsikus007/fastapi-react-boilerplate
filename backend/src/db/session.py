from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar

from src.core.config import settings


# https://github.com/tiangolo/sqlmodel/issues/189
Select.inherit_cache = True  # type: ignore
SelectOfScalar.inherit_cache = True  # type: ignore

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)  # TODO pool_size=POOL_SIZE, max_overflow=64)

# https://github.com/tiangolo/sqlmodel/issues/54
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore  # TODO autoflush=False
