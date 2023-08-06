from typing import Union

from fastapi import APIRouter

from sqlmodel import select, Session
from app.database import engine, Department

router = APIRouter()


@router.get("/departments", tags=["departments"])
async def retrieve_all_departments():
    with Session(engine) as session:
        statement = select(Department)
        results = session.exec(statement)
        department_list = [[department, department.positions] for department in results]
    return {"results": department_list}
