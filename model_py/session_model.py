from typing import Optional
from dataclasses import dataclass, field
from tkinter import Tk, Label

from model_py.button_data import ButtonData
from model_py.text_label import TextLabel
from model_py.game_data import GameData
from util_py import RootImages


@dataclass
class RootConfig:
    width : int = 400
    height : int = 600
    bg : str = '#222'
    fg : str = '#ccc'
    root : Optional[Tk] = None

@dataclass
class TableConfig:
    cell_width : int = 70
    cell_height : int = 70
    spacing : int = 10
    bg : str = '#111'
    width : int = field(init=False)
    height : int = field(init=False)
    label : Optional[Label] = None

    def __post_init__(self):
        self.width = self.cell_width * 3 + self.spacing * 4
        self.height = self.cell_height * 3 + self.spacing * 4

@dataclass
class WidgetUI:
    play_button : Optional[ButtonData] = None
    restart_button : Optional[ButtonData] = None
    label_info : Optional[TextLabel] = None
    rules_panel : Optional[Label] = None

@dataclass
class GameSession:
    root_config : RootConfig = field(default_factory=RootConfig)
    table : TableConfig = field(default_factory=TableConfig)
    ui_widget : WidgetUI = field(default_factory=WidgetUI)
    images : RootImages = field(default_factory=dict)
    game_data : GameData = field(default_factory=GameData)

