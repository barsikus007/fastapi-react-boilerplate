from datetime import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class BaseSchemaRead(BaseSchema):
    id: int
    date_create: datetime
    date_update: datetime
