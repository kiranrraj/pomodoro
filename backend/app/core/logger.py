from loguru import logger
import sys
import os

LOG_LEVEL = "DEBUG" if os.getenv("APP_ENV", "dev") == "dev" else "INFO"

# Remove default handler
logger.remove()

logger.add(
    sys.stderr,
    level=LOG_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}:{function}:{line}</cyan> - <level>{message}</level>"
)

log_path = os.path.join("logs", "app.log")
os.makedirs("logs", exist_ok=True)
logger.add(log_path, rotation="1 week", retention="1 month", level=LOG_LEVEL)

log = logger
