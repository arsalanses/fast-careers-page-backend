from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship, Column, String
from datetime import datetime

class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Column(String(255))
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


class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    application_date: datetime = Field(default=datetime.now())

    jobseeker_name: str
    jobseeker_phone: str
    jobseeker_mail: str
    jobseeker_resume: str

    is_pending: Optional[bool] = True
    is_approved: Optional[bool] = False

    position_id: Optional[int] = Field(default=None, foreign_key="position.id")
    # position: Optional[Position] = Relationship(back_populates="applications")
