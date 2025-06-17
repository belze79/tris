from dataclasses import dataclass
from typing import Optional, Callable
from tkinter import Label, Frame, PhotoImage, Widget
from functools import partial

from enum_py import ButtonType, PlayerType


@dataclass
class ButtonData:
    type : ButtonType
    widget : Optional[Label | Frame] = None
    row : Optional[int] = None
    column : Optional[int] = None
    active : bool = False
    selected : bool = False
    player_type : Optional[PlayerType] = None
    on_enter : Optional[Callable] = None
    on_leave : Optional[Callable] = None
    on_click : Optional[Callable] = None

    def change_state(self):
        self.active = not self.active

    def change_selected(self):
        self.selected = not self.selected

    def change_image(self, image : PhotoImage, cursor : str = ''):
        if not self.widget: return
        self.widget.configure(image=image, cursor=cursor)

    def grid_widget(self):
        if self.row is None or self.column is None: return
        self.widget.grid(row=self.row, column=self.column)

    def apply_event(self):
        if not self.widget: return

        if self.on_enter:
            self.widget.bind('<Enter>', partial(self.on_enter, self))
        if self.on_leave:
            self.widget.bind('<Leave>', partial(self.on_leave, self))
        if self.on_click:
            self.widget.bind('<Button-1>', partial(self.on_click, self))

    def set_player_type(self, player_type : PlayerType):
        self.player_type = player_type

    def switch_button(self, to_show : Widget):
        if self.widget.winfo_viewable():
            self.widget.grid_remove()
            to_show.grid()