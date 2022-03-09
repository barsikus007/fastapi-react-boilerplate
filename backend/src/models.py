from sqlmodel import SQLModel, Field


__all__ = ['Student']


class StudentBase(SQLModel):
    name: str = Field(index=True)
    year: int
    major: str


class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int
