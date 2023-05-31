from uuid import UUID
from typing import Any, Generic, Type, TypeVar
from datetime import datetime, timezone

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Params
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.sqlalchemy import count_query
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select

from src.models.base import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
T = TypeVar("T", bound=Base)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        """
        self.model = model

    async def get(
            self, db: AsyncSession, *,
            id_: int | str | UUID,
    ) -> ModelType | None:
        return await db.get(self.model, id_)

    async def get_count(self, db: AsyncSession) -> ModelType:
        response = await db.execute(count_query(select(self.model)))
        return response.scalars().one()

    async def get_multi(
            self, db: AsyncSession, *,
            params: Params, query: Select | None = None,
    ) -> AbstractPage[ModelType]:
        if query is None:
            query = select(self.model)
        return await paginate(db, query, params)

    async def create(
            self, db: AsyncSession, *,
            obj_in: CreateSchemaType,
    ) -> ModelType:
        obj_db = self.model.from_orm(obj_in)
        db.add(obj_db)
        await db.commit()
        await db.refresh(obj_db)
        return obj_db

    async def update(
            self, db: AsyncSession, *,
            obj_db: ModelType, obj_in: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        obj_data = jsonable_encoder(obj_db)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])
        # TODO psql triggers when update
        setattr(obj_db, "date_update", datetime.now(timezone.utc))
        db.add(obj_db)
        await db.commit()
        await db.refresh(obj_db)
        return obj_db

    async def remove(
            self, db: AsyncSession, *,
            id_: int | str | UUID,
    ) -> ModelType | None:
        obj = await db.get(self.model, id_)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj
