from dataclasses import dataclass, field

from util_py import WinnerCombinations, TableButtons

@dataclass
class GameData:
    winner_combinations : WinnerCombinations = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))
    )
    table_buttons : TableButtons = field(default_factory=dict)
    game_over : bool = True
    animation : bool = False