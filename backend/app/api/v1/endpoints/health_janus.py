# /backend/app/api/v1/endpoints/health_janus.py
from fastapi import APIRouter
from app.db.janus import ping_janusgraph
from loguru import logger

router = APIRouter(prefix="/health/janus", tags=["JanusGraph Health"])

@router.get("", summary="Check JanusGraph connection status")
async def janusgraph_status():
    healthy = ping_janusgraph()
    if healthy:
        logger.info("JanusGraph is reachable.")
        return {"status": "ok", "message": "JanusGraph is reachable"}
    else:
        logger.error("JanusGraph is NOT reachable.")
        return {"status": "error", "message": "JanusGraph is not reachable"}
