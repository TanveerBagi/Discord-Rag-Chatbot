import logging
from rich.logging import RichHandler
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Format: 2025-07-11 16:45:32
    handlers=[
        RichHandler(),
        logging.FileHandler("logs/chatbot.log")
    ]
)

logger = logging.getLogger("discord_rag_bot")
