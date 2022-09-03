from datetime import datetime

from sqlmodel import SQLModel, Field, Column, DateTime, func


class Base(SQLModel):
    id: int | None = Field(primary_key=True)
    date_create: datetime | None = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    date_update: datetime | None = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    # TODO https://stackoverflow.com/questions/70946151/how-to-set-default-on-update-current-timestamp-in-postgres-with-sqlalchemy
    # TODO Field(sa_column=Column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))


# TODO: Why?
# CourseReadWithLinks.update_forward_refs()
# StudentReadWithLinks.update_forward_refs()
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
