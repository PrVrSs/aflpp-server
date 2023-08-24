import asyncio
import os
import re
from dataclasses import dataclass
from typing import Optional, TypedDict

import aiofiles


ASAN_REGEX_1 = re.compile(
    r'^==\d+==ERROR: AddressSanitizer: (?P<BugType>\S+) (?P<Detail>.*)$',
    flags=re.MULTILINE,
)
ASAN_REGEX_2 = re.compile(
    r'^==\d+==AddressSanitizer:? (?P<BugType>[^:]+): (?P<Detail>.*)$',
    flags=re.MULTILINE,
)


class AsanReport(TypedDict):
    raw: str
    bug_type: str
    detail: str


@dataclass
class CrashReport:
    report: AsanReport


def parse_error(error: str) -> Optional[AsanReport]:
    if parsed := (ASAN_REGEX_1.search(error) or ASAN_REGEX_2.search(error)):
        return AsanReport(
            raw=error,
            bug_type=parsed.group('BugType'),
            detail=parsed.group('Detail'),
        )


class Replay:
    def __init__(self, binary_path, binary_args, stdin_file, timeout):
        self._binary_path = binary_path
        self._stdin_file = stdin_file
        self._binary_args = binary_args
        self._timeout = timeout

        self._is_hang = False
        self._process = None

        self.report = None

    @property
    def has_crashed(self) -> bool:
        if self._process.returncode:
            return self._process.returncode != 0

        return False

    @property
    def is_asan_without_crash(self) -> bool:
        return self._report is not None and not self.has_crashed

    @property
    def return_code(self) -> int:
        return self._process.returncode

    async def _make_report(self):
        _, errs = await self._run_proc(input_=await self._read_stdin_file())

        parsed_errs = parse_error(errs.decode())
        if parsed_errs is None:
            return

        self.report = CrashReport(report=parsed_errs)

    async def _create_proc(self):
        self._process = await asyncio.create_subprocess_exec(
            self._binary_path, *self._binary_args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=os.environ.copy(),
        )

    async def _read_stdin_file(self):
        async with aiofiles.open(self._stdin_file, mode='rb') as fp:
            return await fp.read()

    async def _run_proc(self, input_):
        try:
            return await asyncio.wait_for(self._process.communicate(input=input_), timeout=self._timeout)
        except asyncio.exceptions.TimeoutError:
            self._is_hang = True
            self._process.kill()
            return b'', b''

    def __await__(self):
        return self.__await_impl__().__await__()

    async def __await_impl__(self):
        await self._create_proc()
        await self._make_report()

        return self


async def make_replay(
    binary_path: str,
    binary_args: Optional[list[str]] = None,
    stdin_file=None,
    timeout=1,
) -> Replay:
    return await Replay(
        binary_path=binary_path,
        stdin_file=stdin_file,
        timeout=timeout,
        binary_args=binary_args or [],
    )
