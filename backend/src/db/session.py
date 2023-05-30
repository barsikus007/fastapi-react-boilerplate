from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.config import settings


engine = create_async_engine(
    settings.DATABASE_URL, echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE, max_overflow=settings.MAX_OVERFLOW)

SessionLocal = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
