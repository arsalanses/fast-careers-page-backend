from fastapi import APIRouter

router = APIRouter()


@router.get("/positions")
async def root():
    return {"message": "Hello Bigger Applications!"}
