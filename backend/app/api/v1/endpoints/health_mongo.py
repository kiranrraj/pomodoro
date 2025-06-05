# /backend/app/api/v1/endpoints/health_mongo.py
from fastapi import APIRouter
from app.db.mongo import get_db
from pymongo.errors import PyMongoError
from loguru import logger

router = APIRouter(prefix="/health/mongo", tags=["MongoDB Health"])

@router.get("")
async def mongo_status():
    try:
        db = get_db()
        result = db.command("ping")
        if result.get("ok") == 1.0:
            return {"status": "ok", "message": "MongoDB is alive"}
        else:
            logger.error("MongoDB ping failed")
            return {"status": "fail", "message": "MongoDB did not respond to ping"}
    except PyMongoError as e:
        logger.exception("MongoDB connection error")
        return {"status": "error", "message": "Failed to connect to MongoDB"}
