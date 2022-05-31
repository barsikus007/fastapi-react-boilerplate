import asyncio

from sqlmodel.ext.asyncio.session import AsyncSession

from src import crud
from src.db.session import SessionLocal
from src.core.config import settings
from src.schemas.user import IUserCreate


async def init_db(db: AsyncSession) -> None:
    user = await crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = IUserCreate(
            name=settings.FIRST_SUPERUSER_NAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = await crud.user.create(db, obj_in=user_in)


async def main() -> None:
    async with SessionLocal() as session:
        await init_db(session)


if __name__ == '__main__':
    asyncio.run(main())
