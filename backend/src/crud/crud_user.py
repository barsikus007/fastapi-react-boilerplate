from typing import Any

from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models.user import User
from src.schemas.user import IUserCreate, IUserUpdate
from src.core.security import verify_password, get_password_hash


class CRUDUser(CRUDBase[User, IUserCreate, IUserUpdate]):
    async def get_by_email(
            self, db: AsyncSession, *,
            email: str,
    ) -> User | None:
        users = await db.execute(select(User).where(User.email == email))
        return users.scalars().first()

    async def create(
            self, db: AsyncSession, *,
            obj_in: IUserCreate,
    ) -> User:
        obj_in_data = jsonable_encoder(obj_in, exclude={"password"})
        obj_in_data["hashed_password"] = get_password_hash(obj_in.password)
        obj_db = self.model(**obj_in_data)
        db.add(obj_db)
        await db.commit()
        await db.refresh(obj_db)
        return obj_db

    async def update(
            self, db: AsyncSession, *,
            obj_db: User, obj_in: IUserUpdate | dict[str, Any],
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(db, obj_db=obj_db, obj_in=update_data)

    async def authenticate(
            self, db: AsyncSession, *,
            email: EmailStr, password: str,
    ) -> User | None:
        user_auth = await self.get_by_email(db, email=email)
        if not user_auth:
            return None
        if not verify_password(password, user_auth.hashed_password):
            return None
        return user_auth


user = CRUDUser(User)
