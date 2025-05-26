import logging
from rich.logging import RichHandler
import os

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logger = logging.getLogger("scraper")

if not logger.handlers:
    logger.setLevel(log_level)
    
    handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_time=True,
        show_path=False,
        show_level=True
    )
    
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.propagate = False