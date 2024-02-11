# from uuid import uuid4, UUID
from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, declared_attr, mapped_column


# https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#integrating-with-alternate-dataclass-providers-such-as-pydantic
class Base(
        MappedAsDataclass,
        DeclarativeBase,
        kw_only=True,  # type: ignore[call-arg]
):
    @declared_attr.directive
    def __tablename__(cls):  # pylint: disable=no-self-argument
        return cls.__name__.lower()

    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types
    # https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapped-column-derives-the-datatype-and-nullability-from-the-mapped-annotation
    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
    }

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    # id: Mapped[UUID] = mapped_column(default_factory=uuid4, primary_key=True)
    date_create: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    date_update: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())
    # TODO https://stackoverflow.com/questions/70946151/how-to-set-default-on-update-current-timestamp-in-postgres-with-sqlalchemy
    # TODO Mapped[datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


# cascade check
# TODO: Why?
    # student_id: int | None = Field(
    #     foreign_key='student.id', primary_key=True
    # )
    # event_id: int | None = Field(
    #     foreign_key='event.id', primary_key=True
    # )

    # classes: List["Class"] = Relationship(back_populates="enrollments", link_model=Attendance)
    # role: Optional['Role'] = Relationship(back_populates='users')
    # created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin", "primaryjoin":"Group.created_by_id==User.id"})
    # users: List["User"] = Relationship(back_populates="groups", link_model=LinkGroupUser, sa_relationship_kwargs={"lazy": "selectin"})
