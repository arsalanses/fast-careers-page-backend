from fastapi import APIRouter

from sqlmodel import Session
from app.database import engine, Application

router = APIRouter()


@router.post("/applications", response_model=Application, tags=["application"])
async def create_application(application: Application):
    # TODO: Read about MultiClass models
    application.is_approved = None
    
    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
        return application

# from fastapi import APIRouter, UploadFile, File
# from typing import Union
# from sqlmodel.ext.asyncio.session import AsyncSession
# @router.post("/applications", tags=["application"]) # response_model=Application
# async def create_application(application: Application, file: Union[UploadFile, None] = None):
#     application.is_approved = None

#     contents = await file.read()
    
#     async with AsyncSession(engine) as session:
#         async with session.begin():
#             session.add(application)
#             await session.commit()
#             await session.refresh(application)

#     return application
