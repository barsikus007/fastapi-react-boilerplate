from sqlmodel import Field, SQLModel

from src.models.base import Base


class ImageBase(SQLModel):
    name: str
    size: str
    parent: int
    child: int


class Image(ImageBase, Base, table=True):
    file_id: int = Field(default=None, foreign_key='file.id', nullable=False)
