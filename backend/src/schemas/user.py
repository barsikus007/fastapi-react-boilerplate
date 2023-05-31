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


class IUserUpdate(UserBase):  # mypy(error) inherit EmailStr as Optional
    email: EmailStr | None = None  # type: ignore
    password: str | None = None


class IUserUpdateAdmin(IUserUpdate):
    is_superuser: bool
    is_active: bool
