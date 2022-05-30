from uuid import UUID
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlmodel import paginate
from pydantic import BaseModel
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
        self, db: AsyncSession, *, obj_id: Union[str, int]
    ) -> Optional[ModelType]:
        response = await db.get(self.model, obj_id)
        return response

    # async def get_count(
    #     self, db: AsyncSession
    # ) -> Optional[ModelType]:
    #     response = await db.exec(select(func.count()).select_from(select(self.model).subquery()))
    #     return response.one()

    # async def get_multi(
    #     self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    # ) -> List[ModelType]:
    #     response = await db.exec(
    #         select(self.model).offset(skip).limit(limit).order_by(self.model.id)  # type: ignore
    #     )
    #     return response.all()

    async def get_multi_paginated(
        self, db: AsyncSession, *, params: Params, query: T | Select[T] | SelectOfScalar[T] | None = None
    ) -> Page[ModelType]:
        if query is None:
            query = select(self.model)  # type: ignore
        return await paginate(db, query, params)  # type: ignore

    async def create(
        self, db: AsyncSession, *, obj_in: CreateSchemaType
    ) -> ModelType:
        db_obj = self.model.from_orm(obj_in)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: AsyncSession,
        *,
        obj_current: ModelType,
        obj_new: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(obj_current)

        if isinstance(obj_new, dict):
            update_data = obj_new
        else:
            update_data = obj_new.dict(exclude_unset=True) #This tells Pydantic to not include the values that were not sent
        for field in obj_data:
            if field in update_data:
                setattr(obj_current, field, update_data[field])
            if field == "updated_at":
                setattr(obj_current, field, datetime.utcnow())

        db.add(obj_current)
        await db.commit()
        await db.refresh(obj_current)
        return obj_current

    async def remove(
        self, db: AsyncSession, *, obj_id: int | str | UUID
    ) -> ModelType | None:
        obj = await db.get(self.model, obj_id)
        await db.delete(obj)
        await db.commit()
        return obj
