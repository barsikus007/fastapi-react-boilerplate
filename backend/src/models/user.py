from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from src.models.base import Base


class UserBase(SQLModel):
    email: EmailStr = Field(index=True, unique=True)
    name: str | None = None
    phone: str | None = None
    is_superuser: bool = Field(default=False)


class User(UserBase, Base, table=True):
    is_active: bool = Field(default=True)
    hashed_password: str = Field(
        nullable=False, index=True
    )
