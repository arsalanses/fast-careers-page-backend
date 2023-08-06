from fastapi import APIRouter

router = APIRouter()


@router.get("/jobseekers")
async def root():
    return {"message": "Hello Bigger Applications!"}
