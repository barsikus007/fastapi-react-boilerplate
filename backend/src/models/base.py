# from uuid import uuid4, UUID
from datetime import datetime

import pydantic
from sqlalchemy import func, TIMESTAMP
from sqlalchemy.orm import declared_attr, DeclarativeBase, Mapped, mapped_column, MappedAsDataclass


class Base(
        MappedAsDataclass,
        DeclarativeBase,
        dataclass_callable=pydantic.dataclasses.dataclass,
):
    @declared_attr.directive
    def __tablename__(cls):  # pylint: disable=no-self-argument
        return cls.__name__.lower()

    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
    }
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    # id: Mapped[UUID] = mapped_column(default_factory=uuid4, primary_key=True)
    date_create: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    date_update: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), insert_default=func.now())
    # TODO https://stackoverflow.com/questions/70946151/how-to-set-default-on-update-current-timestamp-in-postgres-with-sqlalchemy
    # TODO Mapped[datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


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
