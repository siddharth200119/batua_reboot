from .logger import Logger, logging
import os

_log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper(), logging.INFO)
logger = Logger(service_name=os.environ.get("SERVICE_NAME", "NAMELESS_SERVICE"), level=_log_level)
