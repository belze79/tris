from pygame import mixer as mix

from session import session
from enum_py import SoundType
from util_py import get_asset_path


mix.init()

music_sound = mix.Sound(get_asset_path('assets/sound/loop_sound.wav'))
music_sound.set_volume(0.1)

effect_sounds : dict[SoundType, mix.Sound] = {
    SoundType.PLAY : mix.Sound(get_asset_path('assets/sound/horn_sound.mp3')),
    SoundType.CELL_CLICK : mix.Sound(get_asset_path('assets/sound/click_sound.mp3'))
}

for _sound in effect_sounds.values(): _sound.set_volume(0.3)

def set_volume(current_volume : float, increase : bool) -> float:
    if increase:
        return min(round(current_volume + 0.1, 1), 1)
    else:
        return max(round(current_volume - 0.1, 1), 0)

def set_effect_volume(increase : bool):
    for sound in effect_sounds.values():
        sound.set_volume(set_volume(sound.get_volume(), increase))

def set_music_volume(increase : bool):
    music_sound.set_volume(set_volume(music_sound.get_volume(), increase))



def music_loop():
    music_sound.play()
    session.root_config.root.after(int(music_sound.get_length() * 1000), music_loop)

def click_effect(key : SoundType):
    effect_sounds[key].play()



