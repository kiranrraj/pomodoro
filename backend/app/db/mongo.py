from pymongo import MongoClient, errors
from app.core.config import get_settings
from loguru import logger

settings = get_settings()

# Global variables for reuse
_db = None
_client = None

def init_mongo():
    global _client, _db
    try:
        _client = MongoClient(settings.mongo_uri, serverSelectionTimeoutMS=3000)
        _db = _client["pomodoro_db"]
        _client.admin.command("ping")
        logger.info("MongoDB connected successfully.")
    except errors.PyMongoError as e:
        logger.error("MongoDB connection failed.")
        logger.exception(e)
        _db = None
        _client = None

# Call once at import (early connection attempt)
init_mongo()

def get_db():
    return _db

def ping_mongo() -> bool:
    try:
        if _client is None:
            logger.warning("MongoDB client not initialized.")
            return False
        _client.admin.command("ping")
        return True
    except errors.PyMongoError as e:
        logger.warning(f"MongoDB ping failed: {e}")
        return False
