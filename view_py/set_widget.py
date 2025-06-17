from tkinter import Label, Frame

from session import session
from util_py.image_handler import set_images, get_tkinter_text_image
from view_py import on_enter, on_leave, on_click
from enum_py import ImageType, ButtonType
from model_py.text_label import TextLabel
from model_py.button_data import ButtonData


def set_title(row : int, col : int):
    set_images()
    names : tuple[str, str, str] = 'tic', 'tac', 'toe'
    colors : tuple[str, str, str] = 'green', 'orange', 'red'
    grid = Frame(session.root_config.root, bg=session.root_config.bg)
    grid.grid_columnconfigure((1, 3), minsize=10)
    grid.grid(row=row, column=col)
    for i, (name, color) in enumerate(zip(names, colors)):
        title_image = TextLabel(34, widget=Label(grid, bg=session.root_config.bg), row=0, column=i * 2)
        setattr(title_image.widget, name, get_tkinter_text_image(name, title_image.font_size, color))
        title_image.change_text_image(getattr(title_image.widget, name))
        title_image.grid_label()


def set_table(row : int, col : int):
    session.table.label = Label(session.root_config.root, image=session.images[ImageType.TABLE_IMAGE], bg=session.root_config.bg)
    session.table.label.grid_rowconfigure((0, 2, 4, 6), minsize=session.table.spacing)
    session.table.label.grid_columnconfigure((0, 2, 4, 6), minsize=session.table.spacing)
    session.table.label.grid(row=row, column=col)
    for r in range(3):
        for c in range(3):
            btn : ButtonData = ButtonData(
                ButtonType.CELL,
                widget=Label(session.table.label, image=session.images[ImageType.CELL_NORMAL], bg=session.table.bg),
                row=r * 2 + 1, column=c * 2 + 1,
                on_enter=on_enter, on_leave=on_leave, on_click=on_click
            )
            btn.apply_event()
            btn.grid_widget()
            session.game_data.table_buttons[(r, c)] = btn


def set_label_info(row : int, col : int):
    session.ui_widget.label_info = TextLabel(font_size=20,
                                 widget=Label(session.root_config.root, bg=session.root_config.bg),
                                 row=row, column=col
                                 )
    session.ui_widget.label_info.change_text_image(session.images[ImageType.PRESS_PLAY])
    session.ui_widget.label_info.grid_label()


def set_restart_button(row : int, col : int):
    btn: ButtonData = ButtonData(ButtonType.RESTART,
                                 widget=Label(session.root_config.root, image=session.images[ImageType.RESTART_NORMAL], bg=session.root_config.bg),
                                 row=row, column=col,
                                 on_enter=on_enter, on_leave=on_leave, on_click=on_click
                                 )
    btn.apply_event()
    btn.grid_widget()
    btn.widget.grid_remove()
    session.ui_widget.restart_button = btn

def set_play_button(row : int, col : int):
    btn : ButtonData = ButtonData(ButtonType.PLAY,
                                   widget=Label(session.root_config.root, image=session.images[ImageType.PLAY_NORMAL], bg=session.root_config.bg),
                                   row=row, column=col,
                                   on_enter=on_enter, on_leave=on_leave, on_click=on_click
                                   )
    btn.apply_event()
    btn.grid_widget()
    session.ui_widget.play_button = btn

def set_volume_grid(row : int, col : int):

    main_grid = Frame(session.root_config.root, bg=session.root_config.bg)
    main_grid.grid_rowconfigure(1, minsize=10)
    main_grid.grid(row=row, column=col)

    effect_grid = Frame(main_grid, bg=session.root_config.bg)
    effect_grid.grid(row=0, column=0)

    music_grid = Frame(main_grid, bg=session.root_config.bg)
    music_grid.grid(row=2, column=0)

    less_effect : ButtonData = ButtonData(
        ButtonType.LESS_EFFECT_VOLUME,
        widget=Label(effect_grid, image=session.images[ImageType.LESS_VOLUME_NORMAL], bg=session.root_config.bg, borderwidth=0),
        row=0, column=0,
        on_enter=on_enter, on_leave=on_leave, on_click=on_click
    )
    less_effect.apply_event()
    less_effect.grid_widget()

    text_effect : Label = Label(effect_grid, image=session.images[ImageType.EFFECT_VOLUME_TEXT], bg=session.root_config.bg, borderwidth=0)
    text_effect.grid(row=0, column=1)

    plus_effect: ButtonData = ButtonData(
        ButtonType.PLUS_EFFECT_VOLUME,
        widget=Label(effect_grid, image=session.images[ImageType.PLUS_VOLUME_NORMAL], bg=session.root_config.bg, borderwidth=0),
        row=0, column=2,
        on_enter=on_enter, on_leave=on_leave, on_click=on_click
    )
    plus_effect.apply_event()
    plus_effect.grid_widget()

    less_music: ButtonData = ButtonData(
        ButtonType.LESS_MUSIC_VOLUME,
        widget=Label(music_grid, image=session.images[ImageType.LESS_VOLUME_NORMAL], bg=session.root_config.bg, borderwidth=0),
        row=0, column=0,
        on_enter=on_enter, on_leave=on_leave, on_click=on_click
    )
    less_music.apply_event()
    less_music.grid_widget()

    text_music: Label = Label(music_grid, image=session.images[ImageType.MUSIC_VOLUME_TEXT], bg=session.root_config.bg, borderwidth=0)
    text_music.grid(row=0, column=1)

    plus_music: ButtonData = ButtonData(
        ButtonType.PLUS_MUSIC_VOLUME,
        widget=Label(music_grid,image=session.images[ImageType.PLUS_VOLUME_NORMAL], bg=session.root_config.bg, borderwidth=0),
        row=0, column=2,
        on_enter=on_enter, on_leave=on_leave, on_click=on_click
    )
    plus_music.apply_event()
    plus_music.grid_widget()

def set_window():
    row, col = 1, 1
    set_title(row, col)
    row += 2
    set_table(row, col)
    row += 2
    set_label_info(row, col)
    row += 2
    set_restart_button(row, col)
    set_play_button(row, col)
    row += 2
    set_volume_grid(row, col)


# def set_rules_panel():
#     panel = get_panel()
#     store.rules_panel = Label(store.root, image=panel, bg=store.bg_main)
#     store.rules_panel.image = panel
#     store.rules_panel.grid(row=0, column=0, rowspan=6, columnspan=3, sticky='nsew')
#     store.rules_panel.grid_remove()
#     def toggle_rules():
#         store.rules_panel.grid_remove() if store.rules_panel.winfo_viewable() else store.rules_panel.grid()
#     store.root.bind('<Shift_L>', partial(toggle_rules))


