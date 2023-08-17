from app.database import engine, Application
from fastapi import APIRouter, Form, Header
from fastapi.responses import HTMLResponse
from sqlmodel import Session

router = APIRouter()


@router.post("/applications", tags=["application"])
async def create_application(jobseeker_name: str = Form(),
                             jobseeker_phone: str = Form(),
                             jobseeker_mail: str = Form(),
                             jobseeker_resume: str = Form(),
                             position_id: str = Form(),
                             accept: str = Form()):

    application = Application(jobseeker_name=jobseeker_name,
                              jobseeker_phone=jobseeker_phone,
                              jobseeker_mail=jobseeker_mail,
                              jobseeker_resume=jobseeker_resume,
                              position_id=position_id)

    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
    
    if accept == "text/html":
        return HTMLResponse(content="<b>Application submitted</b>", status_code=200)
    
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
