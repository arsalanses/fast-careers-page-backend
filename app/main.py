from typing import Union

from fastapi import FastAPI, Header

from sqlmodel import SQLModel
from .database import engine
from .routers import departments, applications, positions

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(applications.router)
app.include_router(departments.router)
app.include_router(positions.router)

@app.get("/ping")
def ping(x_forwarded_for: Union[str, None] = Header(default=None)):
    return {"ping": f"pong {x_forwarded_for}"}
