import stat
import tempfile
from pathlib import Path


def create_file(data):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        fp.write(data)
        return fp.name


class Binary:
    def __init__(self, source):
        self._binary = Path(create_file(source))
        self._binary.chmod(stat.S_IRWXU)

    def path(self):
        return str(self._binary)

    def __del__(self):
        self._binary.unlink()
