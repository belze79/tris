from enum import Enum, auto


class ButtonType(Enum):
    CELL = auto()
    PLAY = auto()
    RESTART = auto()
    LESS_EFFECT_VOLUME = auto()
    PLUS_EFFECT_VOLUME = auto()
    LESS_MUSIC_VOLUME = auto()
    PLUS_MUSIC_VOLUME = auto()