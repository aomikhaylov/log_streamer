# Author: Anton Mikhaylov
# Created: 16/08/2020

import asyncio

from aiohttp import web

from app.api.http.handler.log import LogRecordHandler
from app.config import CONFIGURATION

from app.manager.log import LogRecordManager


def start_service() -> None:
    """
    Function builds and starts service
    """

    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    try:
        log_manager = LogRecordManager()
        record_handler = LogRecordHandler(log_manager=log_manager)

        app = web.Application()
        app.router.add_post('/read_log', handler=record_handler.get_list)

        web.run_app(
            app=app,
            host=CONFIGURATION['SERVICE_HOST'],
            port=CONFIGURATION['SERVICE_PORT'],
        )

    except KeyboardInterrupt:
        pass

    finally:
        loop.close()
