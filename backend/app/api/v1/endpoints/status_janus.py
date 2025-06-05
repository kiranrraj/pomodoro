# /backend/app/api/v1/endpoints/status_janusgraph.py
from fastapi import APIRouter
from app.db.janus import ping_janusgraph
from loguru import logger

router = APIRouter(prefix="/health/janus", tags=["JanusGraph Health"])

@router.get("/status", summary="Check JanusGraph status")
async def janusgraph_status():
    healthy = ping_janusgraph()
    if healthy:
        logger.info("JanusGraph ping successful.")
        return {"status": "ok", "message": "JanusGraph is reachable"}
    else:
        logger.error("JanusGraph ping failed.")
        return {"status": "error", "message": "JanusGraph is not reachable"}
