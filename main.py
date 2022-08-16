#!/usr/bin/python3
import time
from dataclasses import dataclass

from pygame import mixer


@dataclass
class SoundEntry:
    key: chr
    sound_file: str

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.key
        if isinstance(other, SoundEntry):
            return other.key == self.key


DATA = [
    SoundEntry("l", "sound/lukas.mp3"),
]

MULTI_CHAR = "sound/wild.mp3"
DEFAULT = "sound/nope.mp3"


def play_sound(sound_file: str):
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.5)


def get_character() -> chr:
    in_str = input("")
    if len(in_str) == 1:
        return list(in_str)[0]
    else:
        return None


if __name__ == '__main__':
    while True:
        c = get_character()
        if c is None:
            play_sound(MULTI_CHAR)
        elif c in DATA:
            index = DATA.index(c)
            play_sound(DATA[index].sound_file)
        else:
            play_sound(DEFAULT)
