from loguru import logger
import sys
import os

LOG_LEVEL = "DEBUG" if os.getenv("APP_ENV", "dev") == "dev" else "INFO"

# Remove default handler
logger.remove()

# Add a better console handler
logger.add(sys.stderr, level=LOG_LEVEL, format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>")

# Optional: also log to file (for debugging or later upload to MinIO)
log_path = os.path.join("logs", "app.log")
os.makedirs("logs", exist_ok=True)
logger.add(log_path, rotation="1 week", retention="1 month", level=LOG_LEVEL)

# Exported for use across the app
log = logger
