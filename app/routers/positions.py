from fastapi import APIRouter, HTTPException

from sqlmodel import Session
from app.database import engine, Position

router = APIRouter()


@router.get("/position/{id}", response_model=Position, tags=["position"])
async def retrieve_one_position(id: int):
    with Session(engine) as session:
        position = session.get(Position, id)
        if not position:
            raise HTTPException(status_code=404, detail="Not found")
        return position
