from app.database import engine, Application
from fastapi import APIRouter, Form, UploadFile
from fastapi.responses import HTMLResponse
from sqlmodel import Session
from typing import Annotated
import aiofiles
import random
import string

router = APIRouter()

@router.post("/applications", tags=["application"])
async def create_application(jobseeker_name: Annotated[str, Form()],
                             jobseeker_phone: Annotated[str, Form()],
                             jobseeker_mail: Annotated[str, Form()],
                             jobseeker_resume: UploadFile | None = None,
                             position_id: str = Form(),
                             accept: str = Form()):

    letters = string.ascii_letters
    numbers = string.digits
    random_prefix = ''.join(random.choice(letters + numbers) for _ in range(10))
    filename = f"{random_prefix}-{jobseeker_resume.filename}"

    async with aiofiles.open(f'app/resume_files/{filename}', 'wb') as out_file:
        content = await jobseeker_resume.read()
        await out_file.write(content)

    application = Application(jobseeker_name=jobseeker_name,
                              jobseeker_phone=jobseeker_phone,
                              jobseeker_mail=jobseeker_mail,
                              jobseeker_resume=filename,
                              position_id=position_id)

    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
    
    if accept == "text/html":
        return HTMLResponse(content="<b>Application submitted</b>", status_code=200)
    
    return application
