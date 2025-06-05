from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from app.core.config import get_settings
from app.core.logger import log

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once on startup
    settings = get_settings()
    print(f"Lifespan startup: ENV loaded = {settings.app_env}")
    yield
    # Runs once on shutdown
    print("Lifespan shutdown")

app = FastAPI(title="Pomodoro App", lifespan=lifespan)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    log.info(f"➡️  {request.method} {request.url.path}")
    try:
        response = await call_next(request)
    except Exception as e:
        log.exception("Unhandled error occurred")
        raise e
    log.info(f"⬅️  {request.method} {request.url.path} - {response.status_code}")
    return response

@app.get("/health")
async def health_check():
    settings = get_settings()
    print(settings)
    return {
        "status": "ok",
        "environment": settings.app_env,
        "mongo_uri": settings.mongo_uri,
        "janusgraph_url": settings.janusgraph_url
    }
