from tkinter import Label
from random import choice

from session import session
from enum_py import MoveType, PlayerType, ImageType


def get_coordinate(empty_length : int, player_length : int, player_type : PlayerType) -> tuple[int, int] | None:
    temp_coordinate: list[tuple[int, int]] = []
    empty_cells = [c for c in session.game_data.table_buttons.keys() if not session.game_data.table_buttons[c].player_type]
    player_type_cells = [c for c in session.game_data.table_buttons.keys() if session.game_data.table_buttons[c].player_type == player_type]
    for combination in session.game_data.winner_combinations:
        cell_empty = [c for c in combination if c in empty_cells]
        cell_player = [c for c in combination if c in player_type_cells]
        if len(cell_empty) == empty_length and len(cell_player) == player_length:
            temp_coordinate += cell_empty
    if not temp_coordinate: return None
    return choice(temp_coordinate)

def get_bot_cell(move_type : MoveType) -> tuple[int, int] | None:
    if move_type == move_type.WIN:
        return get_coordinate(1, 2, PlayerType.BOT)
    elif move_type == move_type.BLOCK:
        return get_coordinate(1, 2, PlayerType.PLAYER)
    elif move_type ==  move_type.STRATEGIC:
        return get_coordinate(2, 1, PlayerType.BOT)
    elif move_type ==  move_type.TACTICAL:
        return get_coordinate(2, 1, PlayerType.PLAYER)
    elif move_type ==  move_type.RANDOM:
        empty_cells = [c for c in session.game_data.table_buttons.keys() if not session.game_data.table_buttons[c].player_type]
        return choice(empty_cells)
    return None


def set_bot_cell(coordinate : tuple[int, int]):
    cell_data = session.game_data.table_buttons[coordinate]
    cell_data.player_type = PlayerType.BOT
    cell_data.state_image = session.images[ImageType.BOT]
    cell_data.selected = True
    cell_data.widget.configure(image=cell_data.state_image, cursor='')

def bot_move():
    for move_type in MoveType:
        cell = get_bot_cell(move_type)
        if cell:
            set_bot_cell(cell)
            return




