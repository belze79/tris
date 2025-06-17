from tkinter import Event
from random import choice

from session import session
from model_py.button_data import ButtonData
from enum_py import PlayerType, ButtonType, ImageType, SoundType
from view_py.ui_function import check_end_game, after_player_move, reset_table
from controller_py import set_music_volume, set_effect_volume, click_effect


def on_enter(btn : ButtonData, e : Event = None):
    match btn.type:
        case ButtonType.LESS_EFFECT_VOLUME | ButtonType.LESS_MUSIC_VOLUME:
            btn.change_image(session.images[ImageType.LESS_VOLUME_HOVER], cursor='hand2')
        case ButtonType.PLUS_EFFECT_VOLUME | ButtonType.PLUS_MUSIC_VOLUME:
            btn.change_image(session.images[ImageType.PLUS_VOLUME_HOVER], cursor='hand2')
        case ButtonType.CELL if not session.game_data.game_over and not session.game_data.animation and not btn.selected:
            btn.change_image(session.images[ImageType.CELL_HOVER], cursor='hand2')
        case ButtonType.RESTART if btn.active:
            btn.change_image(session.images[ImageType.RESTART_HOVER], cursor='hand2')
        case ButtonType.PLAY if session.game_data.game_over:
            btn.change_image(session.images[ImageType.PLAY_HOVER], cursor='hand2')




def on_leave(btn : ButtonData, e : Event = None):

    match btn.type:
        case ButtonType.LESS_EFFECT_VOLUME | ButtonType.LESS_MUSIC_VOLUME:
            btn.change_image(session.images[ImageType.LESS_VOLUME_NORMAL])
        case ButtonType.PLUS_EFFECT_VOLUME | ButtonType.PLUS_MUSIC_VOLUME:
            btn.change_image(session.images[ImageType.PLUS_VOLUME_NORMAL])
        case ButtonType.CELL if not session.game_data.game_over and not session.game_data.animation and not btn.selected:
            btn.change_image(session.images[ImageType.CELL_NORMAL])
        case ButtonType.RESTART if btn.active:
            btn.change_image(session.images[ImageType.RESTART_NORMAL])
        case ButtonType.PLAY if session.game_data.game_over:
            btn.change_image(session.images[ImageType.PLAY_NORMAL])



def on_click(btn : ButtonData, e : Event = None):

    match btn.type:
        case ButtonType.LESS_EFFECT_VOLUME:
            click_effect(SoundType.CELL_CLICK)
            set_effect_volume(increase=False)
        case ButtonType.PLUS_EFFECT_VOLUME:
            click_effect(SoundType.CELL_CLICK)
            set_effect_volume(increase=True)
        case ButtonType.LESS_MUSIC_VOLUME:
            click_effect(SoundType.CELL_CLICK)
            set_music_volume(increase=False)
        case ButtonType.PLUS_MUSIC_VOLUME:
            click_effect(SoundType.CELL_CLICK)
            set_music_volume(increase=True)
        case ButtonType.CELL if not session.game_data.game_over and not session.game_data.animation and not btn.selected:
            session.game_data.animation = True
            click_effect(SoundType.CELL_CLICK)
            btn.change_image(session.images[ImageType.PLAYER])
            btn.change_selected()
            btn.player_type = PlayerType.PLAYER
            check_end_game(PlayerType.PLAYER)
            if not session.game_data.game_over:
                delay = choice([400, 600, 800, 1000, 1200])
                btn.widget.after(delay, after_player_move)
                session.ui_widget.label_info.change_text_image(session.images[ImageType.BOT_MOVE])
        case ButtonType.RESTART if btn.active:
            click_effect(SoundType.CELL_CLICK)
            btn.change_state()
            btn.change_image(session.images[ImageType.RESTART_DISABLE])
            reset_table()
        case ButtonType.PLAY if session.game_data.game_over:
            click_effect(SoundType.PLAY)
            session.game_data.game_over = False
            btn.change_image(session.images[ImageType.PLAY_DISABLE])
            session.ui_widget.label_info.change_text_image(session.images[ImageType.PLAYER_MOVE])
            session.ui_widget.restart_button.change_state()







