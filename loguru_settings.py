import socket
from loguru import logger


HOST = socket.gethostname()

logger.add(
    'logs/logs.log',
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{line} | {message} | " + HOST,
)

