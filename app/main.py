from typing import Union

from fastapi import FastAPI, Header

from sqlmodel import SQLModel
from .database import engine
from .routers import departments, applications, jobseekers, positions

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(applications.router)
app.include_router(departments.router)
app.include_router(jobseekers.router)
app.include_router(positions.router)

@app.get("/ping")
def ping():
    return {"ping": "pong"}

# @app.get("/ip")
# def ip(x_forwarded_for: Union[str, None] = Header(default=None)):
#     return {"ip": x_forwarded_for}
