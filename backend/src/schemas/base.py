from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class BaseSchemaTimestamped(BaseSchema):
    created_at: datetime
    updated_at: datetime


class UUID4BaseSchemaRead(BaseSchemaTimestamped):
    id: UUID


class BaseSchemaRead(BaseSchemaTimestamped):  # TODO: IntBaseSchemaRead
    id: int
