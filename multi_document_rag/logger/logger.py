import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from datetime import datetime
from multi_document_rag.utils.paths import LOG_PATH
import os

try:
    from colorlog import ColoredFormatter
except ImportError:
    raise ImportError("Install colorlog: pip install colorlog")

# os.environ["PYTHONIOENCODING"] = "utf-8"
# os.environ["TERM"] = "xterm-color"

# Config Values
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_CONSOLE_FORMAT = "%(log_color)s[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s"
LOG_LEVEL = logging.DEBUG
LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUP_COUNT = 50
LOG_DIR = os.path.join(LOG_PATH, "logs")

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

#File Handler
file_handler = RotatingFileHandler(
    log_path, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT 
)
file_formatter = logging.Formatter(
    LOG_FILE_FORMAT, 
    datefmt=LOG_DATE_FORMAT
)
file_handler.setFormatter(file_formatter)

# Console Handler
console_handler = StreamHandler()
console_formatter = ColoredFormatter(
    LOG_CONSOLE_FORMAT,
    datefmt=LOG_DATE_FORMAT,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red", 
    }, 
)
console_handler.setFormatter(console_formatter)

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# To stop duplicate logs
logger.propagate = False

if __name__ == "__main__":
    logger.debug("Testing debug log")
    logger.info("Testing info log")
    logger.warning("Testing warning log")
    logger.error("Testing error log")
    logger.critical("Testing critical log")
