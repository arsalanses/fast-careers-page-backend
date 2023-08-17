from app.database import engine, Application
from fastapi import APIRouter, Form, UploadFile
from fastapi.responses import HTMLResponse
from sqlmodel import Session
from typing import Annotated

router = APIRouter()

@router.post("/applications", tags=["application"])
async def create_application(jobseeker_name: Annotated[str, Form()],
                             jobseeker_phone: Annotated[str, Form()],
                             jobseeker_mail: Annotated[str, Form()],
                             jobseeker_resume: UploadFile | None = None,
                             position_id: str = Form(),
                             accept: str = Form()):

    application = Application(jobseeker_name=jobseeker_name,
                              jobseeker_phone=jobseeker_phone,
                              jobseeker_mail=jobseeker_mail,
                              jobseeker_resume=jobseeker_resume.filename,
                              position_id=position_id)

    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
    
    if accept == "text/html":
        return HTMLResponse(content="<b>Application submitted</b>", status_code=200)
    
    return application
