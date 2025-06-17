from dataclasses import dataclass
from typing import Optional
from tkinter import Label, PhotoImage


@dataclass
class TextLabel:
    font_size : int
    widget : Optional[Label] = None
    row : Optional[int] = None
    column : Optional[int] = None

    def change_text_image(self, new_image : PhotoImage):
        if not self.widget : return
        self.widget.configure(image=new_image)

    def grid_label(self):
        if self.row is None or self.column is None: return
        self.widget.grid(row=self.row, column=self.column)