from fastapi import APIRouter

from sqlmodel import Session
from app.database import engine, Application

router = APIRouter()


@router.post("/applications", response_model=Application, tags=["application"])
def create_application(application: Application, tags=["application"]):
    # TODO: Read about MultiClass models
    application.is_approved = None
    
    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
        return application
