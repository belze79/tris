from typing import Tuple, Dict
from tkinter import PhotoImage

from model_py.button_data import ButtonData
from enum_py import ImageType

Coordinate = Tuple[int, int]
Combinations = Tuple[Coordinate, ...]
WinnerCombinations = Tuple[Combinations, ...]

TableButtons = Dict[Coordinate, ButtonData]

RootImages = Dict[ImageType, PhotoImage]