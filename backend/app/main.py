from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from app.core.config import get_settings
from app.core.logger import log
from app.__version__ import __version__

# Import routers
from app.api.v1.endpoints.health_mongo import router as health_mongo_router
from app.api.v1.endpoints.status_mongo import router as status_mongo_router
from app.api.v1.endpoints.health_janus import router as health_janus_router
from app.api.v1.endpoints.status_janus import router as status_janus_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    print(f"Lifespan startup: ENV loaded = {settings.app_env}")
    yield
    print("Lifespan shutdown")

app = FastAPI(title="Pomodoro App", lifespan=lifespan)

# Middleware for request logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    log.info(f"{request.method} {request.url.path}")
    try:
        response = await call_next(request)
    except Exception as e:
        log.exception("Unhandled error occurred")
        raise e
    log.info(f"{request.method} {request.url.path} - {response.status_code}")
    return response

# Core health endpoint
@app.get("/health")
async def health_check():
    settings = get_settings()
    return {
        "status": "ok",
        "version": __version__,
        "environment": settings.app_env,
        "mongo_uri": settings.mongo_uri,
        "janusgraph_url": settings.janusgraph_url,
    }

# Register routers
app.include_router(health_mongo_router)
app.include_router(status_mongo_router)
app.include_router(health_janus_router)
app.include_router(status_janus_router)
