from fastapi import FastAPI

from sqlmodel import SQLModel
from database import engine
from routers import departments, applications, jobseekers, positions

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(applications.router)
app.include_router(departments.router)
app.include_router(jobseekers.router)
app.include_router(positions.router)

@app.get("/ping")
def read_root():
    return {"ping": "pong"}
