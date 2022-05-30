from sqlmodel import SQLModel, Field

from src.models.base import Base


class UserFavoriteBase(SQLModel):
    user_id: int = Field(default=None, foreign_key='user.id', nullable=False)  # TODO test without nullable=False
    image_id: int = Field(default=None, foreign_key='image.id', nullable=False)


class UserFavorite(UserFavoriteBase, Base, table=True):
    pass
