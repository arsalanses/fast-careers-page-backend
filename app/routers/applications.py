from fastapi import APIRouter

router = APIRouter()


@router.get("/applications")
async def root():
    return {"message": "Hello Bigger Applications!"}
