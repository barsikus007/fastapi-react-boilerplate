from sqlmodel import SQLModel, Field


__all__ = ['Student']


class StudentBase(SQLModel):
    name: str
    year: int
    major: str


class Student(StudentBase, table=True):
    id: int = Field(default=None, primary_key=True)


class StudentCreate(StudentBase):
    pass
