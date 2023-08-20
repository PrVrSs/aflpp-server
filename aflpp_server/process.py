import asyncio
import os
import shutil
from pathlib import Path
from typing import Optional

from aflpp_server.logger import logger


BINARY = 'afl-fuzz'
AFLPP_ENV_VAR = 'AFLPP_PATH'


def alfpp_binary(root_dir: Path | str | None = None) -> Optional[Path]:
    if root_dir:
        bin_path = Path(root_dir) / BINARY
        return bin_path if bin_path.exists() else None

    aflpp_path = os.environ.get(AFLPP_ENV_VAR)
    return Path(aflpp_path) / 'afl-fuzz' if aflpp_path else shutil.which(BINARY)


async def capture_program_output(pipe, log):
    while True:
        line = await pipe.readline()
        if not line:
            break

        log(f'[AFL++] {line.decode()}')


class AFLProcess:
    def __init__(self, workspace, aflpp: Optional[str] = None):
        self._workspace = workspace
        self._path = alfpp_binary(aflpp)

        self._process = None
        self._tasks = []

    def aflpp_env_variables(self):
        return {
            'AFL_NO_UI': '1',
            'AFL_QUIET': '1',
            'AFL_IMPORT_FIRST': '1',
            'AFL_AUTORESUME': '1',
            'AFL_SKIP_CPUFREQ': '1',
            'AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES': '1',
        }

    async def run(self, aflpp_arguments, target, target_arguments=None):
        if self._process is not None:
            logger.info('[AFL++] AFL++: running')

        workspace_cmd = [
            '-M', 'main',
            '-i', f'{self._workspace.input_dir}',
            '-F', f'{self._workspace.dynamic_input_dir}',
            '-o', f'{self._workspace.output_dir}',
        ]

        aflpp_cmdline = [
            *aflpp_arguments,
            *workspace_cmd,
            '--',
            target,
            *(target_arguments or [])
        ]

        logger.info(f'[AFL++] Run AFL++: {aflpp_cmdline}')

        self._process = await asyncio.create_subprocess_exec(
            self._path, *aflpp_cmdline,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=os.environ.copy() | self.aflpp_env_variables(),
        )

        self._tasks = [
            asyncio.create_task(capture_program_output(self._process.stdout, logger.info)),
            asyncio.create_task(capture_program_output(self._process.stderr, logger.warning)),
        ]

        logger.debug(f'[AFL++] Process pid: {self._process.pid}')

    async def stop(self):
        if self._process:
            logger.debug(f'[AFL++] Stopping process with pid: {self._process.pid}')
            self._process.kill()
        else:
            logger.debug('[AFL++] AFL++ process seems already killed')

        for task in self._tasks:
            task.cancel()

        await asyncio.gather(*self._tasks, return_exceptions=True)

        self._process = None
