import tempfile
from datetime import datetime
from pathlib import Path

import aiofiles
import attrs
from attrs import define, field
from watchdog.events import (
    DirCreatedEvent,
    DirModifiedEvent,
    FileCreatedEvent,
    FileModifiedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer


def str2float(item: str) -> float:
    return float(item.replace('%', ''))


@define
class Stats:
    start_time: int = field(converter=int)
    last_update: int = field(converter=int)
    run_time: int = field(converter=int)
    fuzzer_pid: int = field(converter=int)
    cycles_done: int = field(converter=int)
    cycles_wo_finds: int = field(converter=int)
    time_wo_finds: int = field(converter=int)
    execs_done: int = field(converter=int)
    execs_per_sec: float = field(converter=float)
    execs_ps_last_min: float = field(converter=float)
    corpus_count: int = field(converter=int)
    corpus_favored: int = field(converter=int)
    corpus_found: int = field(converter=int)
    corpus_imported: int = field(converter=int)
    corpus_variable: int = field(converter=int)
    max_depth: int = field(converter=int)
    cur_item: int = field(converter=int)
    pending_favs: int = field(converter=int)
    pending_total: int = field(converter=int)
    stability: float = field(converter=str2float)
    bitmap_cvg: float = field(converter=str2float)
    saved_crashes: int = field(converter=int)
    saved_hangs: int = field(converter=int)
    last_find: int = field(converter=int)
    last_crash: int = field(converter=int)
    last_hang: int = field(converter=int)
    execs_since_crash: int = field(converter=int)
    exec_timeout: int = field(converter=int)
    slowest_exec_ms: int = field(converter=int)
    peak_rss_mb: int = field(converter=int)
    cpu_affinity: int = field(converter=int)
    edges_found: int = field(converter=int)
    total_edges: int = field(converter=int)
    var_byte_count: int = field(converter=int)
    havoc_expansion: int = field(converter=int)
    auto_dict_entries: int = field(converter=int)
    testcache_size: int = field(converter=int)
    testcache_count: int = field(converter=int)
    testcache_evict: int = field(converter=int)
    afl_banner: str
    afl_version: str
    target_mode: str
    command_line: str


def _parse_stats_line(line: str) -> tuple[str, str]:
    return tuple([
        item.strip()
        for item in line.split(sep=':', maxsplit=1)
    ])


async def read_stat_file(file: str):
    async with aiofiles.open(file, mode='r') as fp:
        return Stats(**dict([
            _parse_stats_line(line)
            async for line in fp
        ]))


class Workspace:

    target_dir = property(fget=lambda self: self.root / 'target')
    input_dir = property(fget=lambda self: self.root / 'inputs' / 'initial')
    dynamic_input_dir = property(fget=lambda self: self.root / 'inputs' / 'dynamic')
    output_dir = property(fget=lambda self: self.root / 'out')
    main_dir = property(fget=lambda self: self.output_dir / 'main')
    corpus_dir = property(fget=lambda self: self.main_dir / 'queue')
    crash_dir = property(fget=lambda self: self.main_dir / 'crashes')
    setup_file = property(fget=lambda self: self.main_dir / 'fuzzer_setup')
    bitmap_file = property(fget=lambda self: self.main_dir / 'fuzz_bitmap')
    stat_file = property(fget=lambda self: self.main_dir / 'fuzzer_stats')

    def __init__(self, queue, root: str = 'afl_agent'):
        self.root = (Path(tempfile.gettempdir()) / root) / datetime.now().strftime('%Y%m%d-%H%M%S')

        self._observer = Observer()
        self._event_handler = AFLFSEventHandler(queue)

        self._init_project()

    def watching(self, path):
        self._observer.schedule(self._event_handler, path=str(path))

    async def get_stats(self):
        return attrs.asdict(await read_stat_file(str(self.stat_file)))

    def _init_project(self):
        for directory in [self.target_dir, self.input_dir, self.dynamic_input_dir, self.corpus_dir, self.crash_dir]:
            directory.mkdir(parents=True)

    def create_seeds(self, seeds: list[bytes]):
        if not seeds:
            seed_path = self.input_dir / 'seed-dummy'
            seed_path.write_bytes(b'init')

        for index, seed in enumerate(seeds):
            seed_path = self.input_dir / f'seed-{index}'
            seed_path.write_bytes(seed)

    def start(self):
        self._observer.start()

    def stop(self):
        self._observer.stop()
        self._observer.join()


class AFLFSEventHandler(FileSystemEventHandler):
    def __init__(self, queue):
        self._queue = queue

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if isinstance(event, FileModifiedEvent):
            self._queue.put(event)

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        if isinstance(event, FileCreatedEvent):
            self._queue.put(event)
