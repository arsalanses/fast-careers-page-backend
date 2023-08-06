from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str

    positions: List["Position"] = Relationship(back_populates="department")


class Position(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    location: str
    experience_level: str

    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    department: Optional[Department] = Relationship(back_populates="positions")

    # applications: List["Application"] = Relationship(back_populates="position")


class JobSeeker(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    contact_details: str
    resume: str

    # applications: List["Application"] = Relationship(back_populates="jobseeker")


class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    application_date: str
    is_pending: Optional[bool] = True
    is_approved: Optional[bool] = False

    jobseeker_id: Optional[int] = Field(default=None, foreign_key="jobseeker.id")
    # jobseeker: Optional[JobSeeker] = Relationship(back_populates="applications")

    position_id: Optional[int] = Field(default=None, foreign_key="position.id")
    # position: Optional[Position] = Relationship(back_populates="applications")
