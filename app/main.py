from typing import Union

from fastapi import FastAPI, Header, Response

from os import environ
from sqlmodel import SQLModel
from .database import engine
from .routers import departments, applications, positions
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

REQUEST_COUNTER = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'path', 'status_code']
)

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
    REQUEST_COUNTER.labels(method='GET', path='/ping', status_code=200).inc()
    return {"ping": f"pong [{environ.get('HOSTNAME')}] -> {x_forwarded_for}"}

@app.get("/metrics")
async def metrics():
    # Generate the latest metrics data in Prometheus format
    data = generate_latest()
    headers = {'Content-Type': CONTENT_TYPE_LATEST}
    return Response(content=data, headers=headers)
