#!/usr/bin/python3
import time
from dataclasses import dataclass
import struct
import sys
from datetime import datetime
from pygame import mixer


@dataclass
class SoundEntry:
    key: int
    sound_file: str

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.key
        if isinstance(other, SoundEntry):
            return other.key == self.key


DATA = [
    SoundEntry(1, "sound/jonas_s_im_studium_lernen.mp3"),  # ESC
    SoundEntry(59, "sound/harry_plus_ist_minus.mp3"),  # F1
    SoundEntry(60, "sound/jonas_s_fresse_halten.mp3"),  # F2
    SoundEntry(61, "sound/jonas_s_jules_ist_qualitaet.mp3"),  # F3
    SoundEntry(62, "sound/jonas_s_laser.mp3"),  # F4
    SoundEntry(63, "sound/jonas_z_es_stinkt.mp3"),  # F5
    SoundEntry(64, "sound/jonas_z_furz.mp3"),  # F6
    SoundEntry(65, "sound/jonas_z_nicht_studiert.mp3"),  # F7
    SoundEntry(66, "sound/jules_big_boobs.mp3"),  # F8
    SoundEntry(67, "sound/lukas.mp3"),  # F9
    SoundEntry(68, "sound/lukas_fox_bms.mp3"),  # F10
    SoundEntry(87, "sound/martin_jeder_macht_was_er_will.mp3"),  # F11
    SoundEntry(88, "sound/sopa.mp3"),  # F12
    SoundEntry(99, "sound/jonas_s_system_is_ready.mp3"),  # PrintScreen
    SoundEntry(70, "sound/Lukas_spannend.mp3"),  # ScrollLock
    SoundEntry(119, "sound/Kristina_Never Gonna Give You Up.mp3"),  # Paus
    SoundEntry(41, "sound/thomas_halloee.mp3"),  # paragraf
    SoundEntry(2, "sound/tobi.mp3"),  # 1
    SoundEntry(3, "sound/Lukas_cad.mp3"),  # 2
    SoundEntry(4, "sound/Lukas_strom_sieg.mp3"),  # 3
    SoundEntry(5, "sound/bayram_koppelweg.mp3"),  # 4
    SoundEntry(6, "sound/bayram_signalintegritaet.mp3"),  # 5
    SoundEntry(7, "sound/thomas_plus_an_minus.mp3"),  # 6
    SoundEntry(8, "sound/jonas_s_kaffi.mp3"),  # 7
    SoundEntry(9, "sound/jonas_s_viel_erfolg.mp3"),  # 8
    SoundEntry(10, "sound/kristina__limbo_fritig.mp3"),  # 9
    SoundEntry(15, "sound/kristina_blblb.mp3"),  # TAB
    SoundEntry(16, "sound/lukas_alu_staub.mp3"),  # Q
    SoundEntry(17, "sound/lukas_traust_dich_eh_nicht.mp3"),  # W
    SoundEntry(18, "sound/martin_gehen_wir_kaffee.mp3"),  # E
    SoundEntry(19, "sound/timon_rooobin.mp3"),  # R
    SoundEntry(20, "sound/timon_schnaebig.mp3"),  # T
    SoundEntry(21, "sound/wyssmann_sitzung.mp3"),  # Z
    SoundEntry(22, "sound/wyssmann_mandelbaerli.mp3"),  # U
    SoundEntry(23, "sound/wyssmann_diode.mp3"),  # I
    SoundEntry(24, "sound/morf_zuegeln.mp3"),  # O
    SoundEntry(25, "sound/morf_stecker_lvdu.mp3"),  # P
    SoundEntry(26, "sound/morf_neuer_print.mp3"),  # U
    SoundEntry(30, "sound/wyssmann_support.mp3"),  # a
    SoundEntry(31, "sound/francesco_bestueckungsliste.mp3"),  # s
    SoundEntry(32, "sound/harry_ach_kinder.mp3"),  # d
    SoundEntry(33, "sound/lukas_endlich_mit_profis.mp3"),  # f
    SoundEntry(34, "sound/oli_sparen.mp3"),  # g
    SoundEntry(35, "sound/lukas.mp3"),  # h
    SoundEntry(36, "sound/Harry_autobatterie.mp3"),  # j
    SoundEntry(37, "sound/Lukas_keyuser.mp3"),  # k
    SoundEntry(38, "sound/Lukas_mimimi.mp3"),  # l
    SoundEntry(39, "sound/Lukas_motor.mp3"),  # oe
    SoundEntry(40, "sound/Lukas_poweruser.mp3"),  # ae
    SoundEntry(81, "sound/thomas_geld_schwimmen.mp3"),  # num3
    SoundEntry(42, "sound/thomas_gruezzi_behring.mp3"),  # shift
    SoundEntry(70, "sound/jonas_s_laser.mp3"),  # Space
    SoundEntry(44, "sound/morf_cost_down.mp3"),  # Y
    SoundEntry(45, "sound/morf_bobcat.mp3"),  # x
    SoundEntry(46, "sound/morf_anforderungen_print.mp3"),  # c
    SoundEntry(47, "sound/meuti_100v.mp3"),  # v
    SoundEntry(48, "sound/josia_von_anfang_an_gedacht.mp3"),  # b
    SoundEntry(49, "sound/josia_stolz.mp3"),  # n
    SoundEntry(50, "sound/josia_kunde_ist_interessiert.mp3"),  # m
    SoundEntry(51, "sound/josia_kann_man_so_machen.mp3"),  # ,
    SoundEntry(52, "sound/josia_alu_ist_dreck.mp3"),  # .
    SoundEntry(53, "sound/bayram_tschaeddere.mp3"),  # -
    SoundEntry(71, "sound/Josia_volvo_knie.mp3"),  # num7
    SoundEntry(72, "sound/Josia_strom_sieg.mp3"),  # num8
    SoundEntry(73, "sound/morf_low_hanging_fruit.mp3"),  # num9
    SoundEntry(76, "sound/thomas_flugzeuge.mp3"),  # num5
    SoundEntry(77, "sound/thomas_leben_am_limit.mp3"),  # num6
    SoundEntry(79, "sound/thomas_staege_am_mentig.mp3"),  # num1
    SoundEntry(80, "sound/thomas_unterschied_mdc22_mdc44.mp3"),  # num2
    SoundEntry(75, "sound/Tibor_Jira.mpeg"),  # num4
    SoundEntry(82, "sound/Tibor_Bullshit.mpeg"),  # num0
]

WELCOME = "sound/sexy_stimme_hallo_robin.mp3"
MULTI_CHAR = "sound/wild.mp3"
DEFAULT = "sound/nope.mp3"


def play_sound(sound_file: str):
    mixer.init(frequency=48000, size=-16, channels=1, buffer=1024)
    mixer.music.load(sound_file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.5)


def get_character(k) -> int:
    # The struct format reads (small L) (small L) (capital H) (capital H) (capital I)
    # Per Python, the structure format codes are as follows:
    # (small L) l - long
    # (capital H) H - unsigned short
    # (capital I) I - unsigned int
    structFormat = 'llHHI'
    eventSize = struct.calcsize(structFormat)

    event = k.read(eventSize)
    goingOn = True
    while goingOn and event:
        (seconds, microseconds, eventType, eventCode, value) = struct.unpack(structFormat, event)

        # Per Linux docs at https://www.kernel.org/doc/html/v4.15/input/event-codes.html
        # Constants defined in /usr/include/linux/input-event-codes.h
        # EV_KEY (1) constant indicates a keyboard event. Values are:
        # 1 - the key is depressed.
        # 0 - the key is released.
        # 2 - the key is repeated.

        # The code corresponds to which key is being pressed/released.

        # Event codes EV_SYN (0) and EV_MSC (4) appear but are not used, although EV_MSC may
        # appear when a state changes.

        if 1 == eventType and value == 1:
            return eventCode

        event = k.read(eventSize)


def GetKeyboardEventFile(tokenToLookFor):
    # Any exception raised here will be processed by the calling function.
    section = ""
    line = ""
    eventName = ""

    fp = open("/proc/bus/input/devices", "r")
    done = False
    while False == done:
        line = fp.readline()
        if line:
            # print (line.strip())
            if "" == line.strip():
                # print ("\nFound Section:\n" + section)
                if -1 != section.find(tokenToLookFor) and -1 == section.lower().find("mouse"):
                    # It is entirely possible there to be multiple devices
                    # listed as a keyboard. In this case, I will look for
                    # the word "mouse" and exclude anything that contains
                    # that. This section may need to be suited to taste
                    print("Found [" + tokenToLookFor + "] in:\n" + section)
                    # Get the last part of the "Handlers" line:
                    lines = section.split('\n')
                    for sectionLine in lines:
                        # The strip() method is needed because there may be trailing spaces
                        # at the end of this line. This will confuse the split() method.
                        if -1 != sectionLine.strip().find("Handlers=") and "" == eventName:
                            print("Found Handlers line: [" + sectionLine + "]")
                            sectionLineParts = sectionLine.strip().split(' ')
                            eventName = sectionLineParts[-1]
                            print("Found eventName [" + eventName + "]")
                            done = True
                section = ""
            else:
                section = section + line
        else:
            done = True
    fp.close()

    if "" == eventName:
        raise Exception("No event name was found for the token [" + tokenToLookFor + "]")

    return "/dev/input/" + eventName


if __name__ == '__main__':
    keyboardEventFile = ""
    try:
        keyboardEventFile = GetKeyboardEventFile("EV=120013")
    except Exception as err:
        print("Couldn't get the keyboard event file due to error [" + str(err) + "]")

    k = open(keyboardEventFile, "rb")

    play_sound(WELCOME)

    time_finished = datetime.now()

    while True:
        c = get_character(k)
        print(f"## got key: {c}")
        if (datetime.now() - time_finished).total_seconds() < 0.2:
            play_sound(MULTI_CHAR)
        elif c in DATA:
            index = DATA.index(c)
            play_sound(DATA[index].sound_file)
        else:
            play_sound(DEFAULT)
        time_finished = datetime.now()
