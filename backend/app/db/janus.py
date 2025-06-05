# /backend/app/db/janus.py
from gremlin_python.driver import client, serializer
from app.core.config import get_settings
from loguru import logger

settings = get_settings()

try:
    janus_client = client.Client(
        settings.janusgraph_url,
        "g",
        username="",
        password="",
        message_serializer=serializer.GraphSONSerializersV3d0()
    )
    logger.info("JanusGraph client initialized.")
except Exception as e:
    janus_client = None
    logger.error("Failed to initialize JanusGraph client.")
    logger.exception(e)

def ping_janusgraph() -> bool:
    if not janus_client:
        return False
    try:
        janus_client.submit("g.V().limit(1)").all().result()
        return True
    except Exception as e:
        logger.error("JanusGraph ping failed.")
        logger.exception(e)
        return False
