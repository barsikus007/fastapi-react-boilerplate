from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from src.models.base import Base


class UserBase(SQLModel):
    name: str
    email: EmailStr = Field(nullable=True, index=True, sa_column_kwargs={'unique': True})
    phone: str | None
    password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)


class User(UserBase, Base, table=True):
    hashed_password: str = Field(
        nullable=False, index=True
    )
