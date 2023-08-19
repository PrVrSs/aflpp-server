import tempfile
from datetime import datetime
from pathlib import Path

from watchdog.events import (
    DirCreatedEvent,
    DirModifiedEvent,
    FileCreatedEvent,
    FileModifiedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer


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
    stats_file = property(fget=lambda self: self.main_dir / 'fuzzer_stats')

    def __init__(self, queue, root: str = 'afl_agent'):
        self.root = (Path(tempfile.gettempdir()) / root) / datetime.now().strftime('%Y%m%d-%H%M%S')

        self._observer = Observer()
        self._event_handler = AFLFSEventHandler(queue)

        self._init_project()

    def watching(self, path):
        self._observer.schedule(self._event_handler, path=str(path))

    def _init_project(self):
        for directory in [self.target_dir, self.input_dir, self.dynamic_input_dir, self.corpus_dir, self.crash_dir]:
            directory.mkdir(parents=True)

        seed_path = self.input_dir / 'seed-dummy'
        seed_path.write_bytes(b'u 4 capsme')

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
