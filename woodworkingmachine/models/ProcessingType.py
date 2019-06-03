from enum import Enum, auto


class ProcessingType(Enum):
    TAPS = auto()
    DRILL = auto()
    SCANS = auto()