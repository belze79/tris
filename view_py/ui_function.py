from random import choice

from session import session
from enum_py import PlayerType, ImageType
from controller_py.bot_function import bot_move


def check_end_game(player_type : PlayerType):
    if not session.game_data.game_over:
        text_image = session.images[ImageType.PLAYER_WIN] if player_type == PlayerType.PLAYER else session.images[ImageType.BOT_WIN]
        for combination in session.game_data.winner_combinations:
            if all(session.game_data.table_buttons[c].player_type == player_type for c in combination):
                session.game_data.game_over = True
                session.ui_widget.label_info.change_text_image(text_image)
                session.ui_widget.restart_button.change_image(session.images[ImageType.RESTART_NORMAL])
                session.ui_widget.play_button.switch_button(session.ui_widget.restart_button.widget)
                return
        if all(session.game_data.table_buttons[c].player_type for c in session.game_data.table_buttons.keys()):
            session.game_data.game_over = True
            session.ui_widget.label_info.change_text_image(session.images[ImageType.DRAW])
            session.ui_widget.play_button.change_image(session.images[ImageType.PLAY_NORMAL])
            session.ui_widget.restart_button.change_image(session.images[ImageType.RESTART_NORMAL])
            session.ui_widget.play_button.switch_button(session.ui_widget.restart_button.widget)


def after_player_move():
    bot_move()
    check_end_game(PlayerType.BOT)
    session.game_data.animation = False
    if not session.game_data.game_over:
        session.ui_widget.label_info.change_text_image(session.images[ImageType.PLAYER_MOVE])

def reset_table():
    buttons = session.game_data.table_buttons
    bot_cell = [buttons[c] for c in buttons.keys() if buttons[c].player_type == PlayerType.BOT]
    player_cell = [buttons[c] for c in buttons.keys() if buttons[c].player_type == PlayerType.PLAYER]

    if not bot_cell and not player_cell:
        session.game_data.animation = False
        session.ui_widget.label_info.change_text_image(session.images[ImageType.PRESS_PLAY])
        session.ui_widget.play_button.change_image(session.images[ImageType.PLAY_NORMAL])
        session.ui_widget.restart_button.switch_button(session.ui_widget.play_button.widget)
        return

    btn = choice(bot_cell or player_cell)
    btn.change_selected()
    btn.player_type = None
    btn.change_image(session.images[ImageType.CELL_NORMAL])
    delay = (len(bot_cell) + len(player_cell)) * 100
    btn.widget.after(delay, reset_table)




