from dataclasses import InitVar

from sqlalchemy import false, true
from sqlalchemy.orm import Mapped, mapped_column

from src.core.security import get_password_hash
from src.models.base import Base


# https://github.com/sqlalchemy/sqlalchemy/issues/9493
class User(Base, kw_only=True):
    email: Mapped[str] = mapped_column(index=True, unique=True)
    name: Mapped[str | None]
    phone: Mapped[str | None]
    is_superuser: Mapped[bool] = mapped_column(server_default=false())
    is_active: Mapped[bool] = mapped_column(init=False, server_default=true())

    password: InitVar[str]
    hashed_password: Mapped[str] = mapped_column(index=True, init=False)

    def __post_init__(self, password: str):
        self.hashed_password = get_password_hash(password)
