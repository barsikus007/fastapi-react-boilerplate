from sqlalchemy import true, false
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class User(Base):
    email: Mapped[str] = mapped_column(index=True, unique=True)
    name: Mapped[str | None]
    phone: Mapped[str | None]
    is_superuser: Mapped[bool] = mapped_column(server_default=false())
    is_active: Mapped[bool] = mapped_column(init=False, server_default=true())
    hashed_password: Mapped[str] = mapped_column(index=True)
