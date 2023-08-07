from fastapi import APIRouter, HTTPException

from sqlmodel import Session
from app.database import engine, Position

router = APIRouter()


@router.get("/position/{position_id}", response_model=Position, tags=["position"])
async def retrieve_one_position(position_id: int):
    with Session(engine) as session:
        position = session.get(Position, position_id)
        if not position:
            raise HTTPException(status_code=404, detail="Not found")
        return position
