from sqlmodel import SQLModel, Field


__all__ = ["User"]


class UserBase(SQLModel):
    name: str = Field(index=True)
    year: int
    major: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
