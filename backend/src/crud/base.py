from uuid import UUID
from typing import Any, Generic, Type, TypeVar
from datetime import datetime

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Params
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.async_sqlmodel import paginate
from sqlmodel import SQLModel, select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
T = TypeVar("T", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLModel model class
        """
        self.model = model

    async def get(
            self, db: AsyncSession, *, id_: str | int
    ) -> ModelType | None:
        return await db.get(self.model, id_)

    async def get_count(self, db: AsyncSession) -> ModelType | None:
        # https://github.com/tiangolo/sqlmodel/issues/54
        response = await db.exec(select(func.count()).select_from(select(self.model).subquery()))  # type: ignore
        return response.one()

    async def get_multi(
            self, db: AsyncSession, *, params: Params,
            query: ModelType | Select[ModelType] | SelectOfScalar[ModelType] | None = None,
    ) -> AbstractPage[ModelType]:
        if query is None:  # Pylance(reportGeneralTypeIssues)
            query = self.model  # type: ignore
        return await paginate(db, query, params)  # type: ignore

    async def create(
            self, db: AsyncSession, *, obj_in: CreateSchemaType
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
            # TODO timezone aware
            if field == "updated_at":
                setattr(obj_db, field, datetime.utcnow())
        db.add(obj_db)
        await db.commit()
        await db.refresh(obj_db)
        return obj_db

    async def remove(
            self, db: AsyncSession, *, id_: int | str | UUID
    ) -> ModelType | None:
        obj = await db.get(self.model, id_)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj
