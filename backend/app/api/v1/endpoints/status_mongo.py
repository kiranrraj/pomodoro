# /backend/app/api/v1/endpoints/status_mongo.py
from fastapi import APIRouter
from app.db.mongo import ping_mongo
from loguru import logger

router = APIRouter(prefix="/health/mongo", tags=["MongoDB Health"])

@router.get("/status", summary="Check MongoDB status")
async def mongo_status():
    healthy = ping_mongo()
    if healthy:
        logger.info("MongoDB ping successful.")
        return {"status": "ok", "message": "MongoDB is reachable"}
    else:
        logger.error("MongoDB ping failed.")
        return {"status": "error", "message": "MongoDB is not reachable"}
