from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.config import settings

engine = create_async_engine(
    str(settings.DATABASE_URL), echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE, max_overflow=settings.MAX_OVERFLOW)

SessionLocal = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
