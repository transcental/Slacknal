import asyncio
import logging

import uvicorn
from dotenv import load_dotenv

from slacknal.config import config

load_dotenv()

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

logging.basicConfig(level="INFO" if config.environment != "production" else "WARNING")


def start():
    uvicorn.run(
        "slacknal.utils.starlette:app",
        host="0.0.0.0",
        port=config.port,
        log_level="info" if config.environment != "production" else "warning",
        reload=config.environment == "development",
    )


if __name__ == "__main__":
    start()
