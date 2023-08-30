import asyncio
from pathlib import Path
from typing import Callable

from watchdog.events import FileCreatedEvent

from aflpp_server.binary import Binary
from aflpp_server.constants import State
from aflpp_server.db import get_session
from aflpp_server.logger import logger
from aflpp_server.models import Report
from aflpp_server.process import AFLProcess
from aflpp_server.replay import make_replay


class AFLPP:
    def __init__(self, workspace, monitor_queue, aflpp_proc: AFLProcess, loop=None):
        self._workspace = workspace
        self._monitor_queue = monitor_queue
        self._loop = loop
        self._aflpp_proc = aflpp_proc
        self._replay_queue = asyncio.Queue()

        self._state = State.NOT_RUNNING

        self._workspace.watching(self._workspace.crash_dir)

        self.fs_handler: dict[str, Callable] = {
            str(self._workspace.crash_dir): (self._crash_handler, FileCreatedEvent),
        }

        self._target = None
        self._tasks = []

    async def start(self, source: bytes, aflpp_args: str, binary_args: str, seeds: list[bytes]) -> bool:
        if self._state == State.RUNNING:
            return False

        logger.info('Start Fuzzer')

        self._target = Binary(source=source)
        self._workspace.create_seeds(seeds)

        await self._aflpp_proc.run(
            target=self._target.path(),
            target_arguments=binary_args.split(),
            aflpp_arguments=aflpp_args.split(),
        )

        await asyncio.sleep(0.2)

        self._workspace.start()
        self._create_tasks()
        self._state = State.RUNNING

        return True

    async def stop(self) -> bool:
        if self._state == State.STOPPED:
            return False

        logger.info('Stop Fuzzer')

        self._workspace.stop()
        await self._aflpp_proc.stop()

        self._monitor_queue.close()
        await self._monitor_queue.wait_closed()
        await self._replay_queue.join()

        for task in self._tasks:
            task.cancel()

        await asyncio.gather(*self._tasks, return_exceptions=True)

        self._state = State.STOPPED
        return True

    async def stats(self):
        return await self._workspace.get_stats()

    async def _replay_task(self):
        while True:
            await self._run_replay(await self._replay_queue.get())
            self._replay_queue.task_done()

    async def _run_replay(self, filename: Path):
        if filename.name == 'README.txt':
            return

        replay = await make_replay(
            binary_path=self._target.path(),
            stdin_file=str(filename),
        )

        async with get_session() as session:
            await Report.add(
                session=session,
                raw=replay.report.report['raw'],
                bug_type=replay.report.report['bug_type'],
                detail=replay.report.report['detail'],
            )

    def _create_tasks(self):
        self._tasks = [
            self._loop.create_task(self._monitor_task(), name='monitor_task'),
            self._loop.create_task(self._replay_task(), name='replay_task'),
        ]

    async def _monitor_task(self):
        while True:
            event = await self._monitor_queue.async_q.get()
            path = Path(event.src_path)

            handler, event_type = self.fs_handler.get(str(path.parent), (None, None))
            if handler is not None and isinstance(event, event_type):
                await handler(filename=path)

            self._monitor_queue.async_q.task_done()

    async def _crash_handler(self, filename: Path):
        await self._replay_queue.put(filename)
