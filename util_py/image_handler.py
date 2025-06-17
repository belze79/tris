from PIL import Image, ImageDraw, ImageTk, ImageFont
from tkinter import PhotoImage

from session import session
from enum_py import PlayerType, ImageType
from util_py import get_asset_path

font_path : str = get_asset_path('assets/font/RobotoCondensed-Bold.ttf')

def get_rounded_image(image : Image.Image, radius : int) -> Image.Image:
    img = image.copy()
    mask = Image.new('L',img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, mask.width, mask.height), radius=radius, fill=255)
    img.putalpha(mask)
    return img

def get_pillow_text_image(text : str, font_size : int, color : str | tuple[int, int, int] | tuple[int, int, int, int]) -> Image.Image:
    enlarged_font = font_size * 16
    font = ImageFont.truetype(font_path, enlarged_font)
    upper_text = text.upper()
    temp_image = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_image)
    x1, y1, x2, y2 = temp_draw.textbbox((0, 0), text=upper_text, font=font)
    tx, ty = x2 - x1, y2 - y1
    text_image = Image.new('RGBA', (int(tx), int(ty)), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, -y1), text=upper_text, font=font, fill=color)
    final = text_image.crop(text_image.getbbox()).resize((tx // 16, ty // 16), Image.Resampling.LANCZOS)
    return final

def get_tkinter_text_image(text : str, font_size : int, color : str | tuple[int, int, int] | tuple[int, int, int, int]) -> PhotoImage:
    pil_image = get_pillow_text_image(text, font_size, color)
    return ImageTk.PhotoImage(pil_image)

def set_table_image():
    w, h = session.table.width, session.table.height
    base = Image.new('RGBA', (w * 8, h * 8), session.table.bg)
    final = get_rounded_image(base, 15 * 8).resize((w, h), Image.Resampling.LANCZOS)
    session.images[ImageType.TABLE_IMAGE] = ImageTk.PhotoImage(final)

def set_empty_cell_state_image():
    w, h = session.table.cell_width, session.table.cell_height
    normal = Image.new('RGBA', (w * 8, h * 8), '#000')
    hover = Image.new('RGBA', normal.size, '#222')
    leave_image = get_rounded_image(normal, 15 * 8).resize((w, h), Image.Resampling.LANCZOS)
    enter_image = get_rounded_image(hover, 15 * 8).resize((w, h), Image.Resampling.LANCZOS)
    session.images[ImageType.CELL_NORMAL] = ImageTk.PhotoImage(leave_image)
    session.images[ImageType.CELL_HOVER] = ImageTk.PhotoImage(enter_image)

def set_player_bot_image():
    w, h = session.table.cell_width, session.table.cell_height
    circle = Image.open(get_asset_path('assets/image/green_circle.png')).resize((60, 60), Image.Resampling.LANCZOS)
    x = Image.open(get_asset_path('assets/image/red_x.png')).resize((50, 50), Image.Resampling.LANCZOS)

    base_circle = Image.new('RGBA', (w * 30, h * 30), 'green')
    base_circle = get_rounded_image(base_circle, 15 * 30).resize((w, h), Image.Resampling.LANCZOS)
    base_x = Image.new('RGBA', base_circle.size, 'red')
    base_x = get_rounded_image(base_x, 15 * 8).resize((w, h), Image.Resampling.LANCZOS)

    alpha_circle = base_circle.split()[3].point(lambda p : int(p * 0.1))
    base_circle.putalpha(alpha_circle)
    base_circle.paste(circle, (5, 5), circle)
    alpha_x = base_x.split()[3].point(lambda p : int(p * 0.1))
    base_x.putalpha(alpha_x)
    base_x.paste(x, (10, 10), x)

    session.images[ImageType.PLAYER] = ImageTk.PhotoImage(base_circle)
    session.images[ImageType.BOT] = ImageTk.PhotoImage(base_x)

def get_states_image(text : str, size : tuple[int, int], font_size : int, bg_color : str, fg_color : str,
                     rounded : bool) -> tuple[PhotoImage, PhotoImage, PhotoImage]:
    _text = text.upper()
    width, height = size

    base = Image.new('RGBA', (width * 8, height * 8), bg_color)
    base = get_rounded_image(base, 25 * 8) if rounded else base

    text_image = get_pillow_text_image(_text, font_size * 8, fg_color)
    text_position = (base.width - text_image.width) // 2, (base.height - text_image.height) // 2
    base.paste(text_image, text_position, text_image)

    hover = base.resize((width, height), Image.Resampling.LANCZOS)
    normal = hover.copy()
    disable = hover.copy()

    alpha_normal = normal.split()[3].point(lambda p : int(p * 0.8))
    normal.putalpha(alpha_normal)
    alpha_disable = disable.split()[3].point(lambda p : int(p * 0.2))
    disable.putalpha(alpha_disable)

    return ImageTk.PhotoImage(hover), ImageTk.PhotoImage(normal), ImageTk.PhotoImage(disable)



def set_volume_button_image(left_text : str, size : tuple[int, int], bg_color : str, fg_color : str):
    width, height = size

    left_hover = Image.new('RGBA', (width * 30, height * 30), bg_color)

    mask = Image.new('L', left_hover.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle((0, 0, mask.width * 2, mask.height), radius=25 * 20, fill=255)
    left_hover.putalpha(mask)

    text_image = get_pillow_text_image(left_text, 20 * 30, fg_color)
    tx_img_position = (left_hover.width - text_image.width) // 2, (left_hover.height - text_image.height) // 2
    left_hover.paste(text_image, tx_img_position, text_image)

    left_hover = left_hover.resize((width, height), Image.Resampling.LANCZOS)
    right_hover = left_hover.rotate(180, expand=True)

    left_normal = left_hover.copy()
    right_normal = right_hover.copy()

    left_alpha = left_normal.split()[3].point(lambda p : int(p * 0.8))
    left_normal.putalpha(left_alpha)
    right_alpha = right_normal.split()[3].point(lambda p : int(p * 0.8))
    right_normal.putalpha(right_alpha)

    session.images[ImageType.LESS_VOLUME_HOVER] = ImageTk.PhotoImage(left_hover)
    session.images[ImageType.LESS_VOLUME_NORMAL] = ImageTk.PhotoImage(left_normal)
    session.images[ImageType.PLUS_VOLUME_HOVER] = ImageTk.PhotoImage(right_hover)
    session.images[ImageType.PLUS_VOLUME_NORMAL] = ImageTk.PhotoImage(right_normal)


def get_panel() -> PhotoImage:
    img = Image.new('RGBA', (session.root_config.width, session.root_config.height), (0, 255, 0))
    alpha = img.split()[3].point(lambda p : int(p * 0.1))
    img.putalpha(alpha)
    return ImageTk.PhotoImage(img)

def set_images():
    font_size = 20
    set_table_image()
    set_empty_cell_state_image()
    set_player_bot_image()
    set_volume_button_image('<<', (30, 20), 'orange', 'yellow')

    session.images[ImageType.PRESS_PLAY] = get_tkinter_text_image('press play to start', font_size, session.root_config.fg)
    session.images[ImageType.PLAYER_WIN] = get_tkinter_text_image(f'{PlayerType.PLAYER.value} WIN!!', font_size, 'green')
    session.images[ImageType.PLAYER_MOVE] = get_tkinter_text_image(f'{PlayerType.PLAYER.value} MOVE!!', font_size, 'green')
    session.images[ImageType.BOT_WIN] = get_tkinter_text_image(f'{PlayerType.BOT.value} WIN!!', font_size, 'red')
    session.images[ImageType.BOT_MOVE] = get_tkinter_text_image(f'{PlayerType.BOT.value} MOVE!!', font_size, 'red')
    session.images[ImageType.DRAW] = get_tkinter_text_image('DRAW!!', font_size, 'orange')

    _, normal_music, _ = get_states_image('music volume', (120, 20), 13, 'orange', 'yellow', rounded=False)
    _, normal_effect, _ = get_states_image('effect volume', (120, 20), 13, 'orange', 'yellow', rounded=False)
    session.images[ImageType.MUSIC_VOLUME_TEXT] = normal_music
    session.images[ImageType.EFFECT_VOLUME_TEXT] = normal_effect

    pl_hover, pl_normal, pl_disable = get_states_image(
        'play', (100, 30), 20, 'green', 'lime', rounded=True)
    restart_hover, restart_normal, restart_disable = get_states_image(
        'restart', (100, 30), 20, 'green', 'lime', rounded=True)
    session.images[ImageType.PLAY_HOVER] = pl_hover
    session.images[ImageType.PLAY_NORMAL] = pl_normal
    session.images[ImageType.PLAY_DISABLE] = pl_disable
    session.images[ImageType.RESTART_HOVER] = restart_hover
    session.images[ImageType.RESTART_NORMAL] = restart_normal
    session.images[ImageType.RESTART_DISABLE] = restart_disable





