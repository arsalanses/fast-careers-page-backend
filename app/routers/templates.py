from fastapi import APIRouter, Request, HTTPException

from sqlmodel import select, Session
from app.database import engine, Department, Position

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    with Session(engine) as session:
        statement = select(Department)
        results = session.exec(statement)
        department_list = [[department, department.positions] for department in results]
    return templates.TemplateResponse("home.html", {"request": request, "results": department_list})

@router.get("/home/position/{position_id}", response_class=HTMLResponse)
async def home(request: Request, position_id: int):
    with Session(engine) as session:
        position = session.get(Position, position_id)
        if not position:
            raise HTTPException(status_code=404, detail="Position not found")
        return templates.TemplateResponse("position.html", {"request": request, "results": position})
