from enum import Enum, auto


class State(Enum):
    NOT_RUNNING = auto()
    RUNNING = auto()
    STOPPED = auto()
