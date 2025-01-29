import re
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import JSON, TIMESTAMP, MetaData, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, declared_attr, mapped_column, registry

orm_registry = registry(
    metadata=MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    ),
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
    # https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapped-column-derives-the-datatype-and-nullability-from-the-mapped-annotation
    type_annotation_map={
        datetime: TIMESTAMP(timezone=True),
        dict: JSON,
    },
)


class ClearBase(
    MappedAsDataclass,
    AsyncAttrs,
    DeclarativeBase,
    kw_only=True,  # type: ignore[call-arg]
):
    registry = orm_registry

    @declared_attr.directive
    def __tablename__(cls):  # pylint: disable=no-self-argument  # noqa: N805
        # https://stackoverflow.com/a/1176023/15844518
        name = cls.__name__  # pylint: disable=no-member
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        name = re.sub("__([A-Z])", r"_\1", name)
        name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
        return name.lower()

    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())  # pylint: disable=not-callable
    updated_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())  # pylint: disable=not-callable
    # TODO https://stackoverflow.com/questions/70946151/how-to-set-default-on-update-current-timestamp-in-postgres-with-sqlalchemy
    # TODO Mapped[datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


# TODO IntBase or BigIntBase https://github.com/litestar-org/advanced-alchemy/blob/main/advanced_alchemy/base.py
class Base(ClearBase, DeclarativeBase):  # TODO: IntBase
    registry = orm_registry

    id: Mapped[int] = mapped_column(init=False, primary_key=True)


class UUID4Base(ClearBase, DeclarativeBase):
    registry = orm_registry

    id: Mapped[UUID] = mapped_column(default_factory=uuid4, primary_key=True)
