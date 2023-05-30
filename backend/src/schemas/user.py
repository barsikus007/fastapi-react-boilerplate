from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    class Config:
        orm_mode = True

    email: EmailStr
    name: str | None = None
    phone: str | None = None


class IUserCreate(UserBase):
    is_superuser: bool = False
    password: str


class IUserRead(UserBase):
    is_superuser: bool
    is_active: bool
    id: int


class IUserUpdate(UserBase):
    password: str


class IUserUpdateAdmin(IUserUpdate):
    is_superuser: bool
    is_active: bool
