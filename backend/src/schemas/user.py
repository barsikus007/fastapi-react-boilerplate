from pydantic import BaseModel, EmailStr

from src.models.user import UserBase


class IUserCreate(UserBase):
    password: str


class IUserRead(UserBase):
    id: int


class IUserUpdate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = True
    name: str | None = None
    phone: str | None = None
