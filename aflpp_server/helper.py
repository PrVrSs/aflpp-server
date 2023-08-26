import asyncio
import functools
import signal

import uvloop

from aflpp_server.logger import logger
from aflpp_server.settings import settings


cleanup_coroutines = []


async def shutdown(signal_=None):
    if signal_:
        logger.info(f'Received exit signal {signal_.name}')

    await asyncio.gather(*cleanup_coroutines, return_exceptions=True)

    tasks = [
        task
        for task in asyncio.all_tasks()
        if task is not asyncio.current_task()
    ]

    for task in tasks:
        task.cancel()

    logger.info(f'Cancelling {len(tasks)} outstanding tasks')

    await asyncio.gather(*tasks, return_exceptions=True)


def set_signal_handler(loop):
    for sig in (signal.SIGHUP, signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(
            sig,
            lambda: loop.create_task(shutdown(sig)),  # pylint: disable=cell-var-from-loop
        )

    loop.set_exception_handler(lambda _, ctx: logger.debug(f'Caught exception: {ctx["message"]}'))


def async_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop, debug=settings.debug) as runner:
            set_signal_handler(loop=runner.get_loop())
            return runner.run(func(*args, **kwargs))

    return wrapper
