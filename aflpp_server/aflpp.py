import asyncio
from pathlib import Path
from typing import Callable

from watchdog.events import FileCreatedEvent

from aflpp_server.binary import Binary
from aflpp_server.logger import logger
from aflpp_server.process import AFLProcess
from aflpp_server.replay import make_replay


class AFLPP:
    def __init__(self, workspace, monitor_queue, aflpp_proc: AFLProcess, loop=None):
        self._workspace = workspace
        self._monitor_queue = monitor_queue
        self._loop = loop
        self._aflpp_proc = aflpp_proc
        self._replay_queue = asyncio.Queue()
        self._workspace.watching(self._workspace.crash_dir)
        self.fs_handler: dict[str, Callable] = {
            str(self._workspace.crash_dir): (self.crash_handler, FileCreatedEvent),
        }

        self._target = None
        self._tasks = []
        self._reports = []

    async def start(self, source: bytes, aflpp_args: str, binary_args: str, seeds: list[bytes]) -> bool:
        logger.info('Start Fuzzer')

        self._target = Binary(source=source)
        self._workspace.create_seeds(seeds)

        await self._aflpp_proc.run(
            target=self._target.path(),
            target_arguments=binary_args.split(),
            aflpp_arguments=aflpp_args.split(),
        )

        self._workspace.start()
        self._tasks = [
            self._loop.create_task(self._monitor_task()),
            self._loop.create_task(self._replay_task()),
        ]

        return True

    async def stop(self):
        logger.info('Stop Fuzzer')
        self._workspace.stop()
        await self._aflpp_proc.stop()

        for task in self._tasks:
            task.cancel()

        await asyncio.gather(*self._tasks, return_exceptions=True)

    async def _replay_task(self):
        while True:
            try:
                await self.run_replay(await self._replay_queue.get())
                self._replay_queue.task_done()
            except asyncio.CancelledError:
                break

    async def run_replay(self, filename: Path):
        if filename.name == 'README.txt':
            return

        replay = await make_replay(
            binary_path=self._target.path(),
            stdin_file=str(filename),
        )
        logger.info(replay.report)
        self._reports.append(replay.report)

    async def _monitor_task(self):
        while True:
            try:
                event = await self._monitor_queue.async_q.get()
                path = Path(event.src_path)

                handler, event_type = self.fs_handler.get(str(path.parent), (None, None))
                if handler is not None and isinstance(event, event_type):
                    await handler(filename=path)

                self._monitor_queue.async_q.task_done()
            except asyncio.CancelledError:
                break

    async def crash_handler(self, filename: Path):
        await self._replay_queue.put(filename)
