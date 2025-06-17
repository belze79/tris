from enum import Enum, auto


class MoveType(Enum):
    WIN = auto()
    BLOCK = auto()
    STRATEGIC = auto()
    TACTICAL = auto()
    RANDOM = auto()