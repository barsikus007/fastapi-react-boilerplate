from sqlmodel import SQLModel

from src.models.base import Base


class FileBase(SQLModel):
    name: str
    path: str


class File(FileBase, Base, table=True):
    pass
