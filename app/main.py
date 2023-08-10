from typing import Union

from fastapi import FastAPI, Header

from os import environ
from sqlmodel import SQLModel
from .database import engine
from .routers import departments, applications, positions

# You can disable docs by setting:
# docs_url=None and redoc_url=None
app = FastAPI(title="Fast Careers Page")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(applications.router)
app.include_router(departments.router)
app.include_router(positions.router)

@app.get("/ping", tags=["health-check"])
def ping(x_forwarded_for: Union[str, None] = Header(default=None)):
    return {"ping": f"pong [{environ.get('HOSTNAME')}] -> {x_forwarded_for}"}
