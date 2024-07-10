from pydantic import EmailStr

from src.schemas.base import BaseSchema, BaseSchemaRead


class UserBase(BaseSchema):
    email: EmailStr
    name: str | None = None
    phone: str | None = None


class IUserCreate(UserBase):
    is_superuser: bool = False
    password: str


class IUserRead(UserBase, BaseSchemaRead):
    is_superuser: bool
    is_active: bool


class IUserUpdate(UserBase):
    email: EmailStr | None = None
    password: str | None = None


class IUserUpdateAdmin(IUserUpdate):
    is_superuser: bool
    is_active: bool
