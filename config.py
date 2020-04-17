# the key settings for playing 88 notes (from A1 to C9)
# (if you have sound files that beyond these range then you can
# modify this dictionary to play them)
key_settings = {
    'z': 'A#2',
    'x': 'B2',
    'c': 'C3',
    'v': 'C#3',
    'b': 'D3',
    'n': 'D#3',
    'm': 'E3',
    ',': 'F3',
    '.': 'F#3',
    '/': 'G3',
    'a': 'G#3',
    's': 'A3',
    'd': 'A#3',
    'f': 'B3',
    'g': 'C4',
    'h': 'C#4',
    'j': 'D4',
    'k': 'D#4',
    'l': 'E4',
    ';': 'F4',
    "'": 'F#4',
    'enter': 'G4',
    'tab': 'G#4',
    'q': 'A4',
    'w': 'A#4',
    'e': 'B4',
    'r': 'C5',
    't': 'C#5',
    'y': 'D5',
    'u': 'D#5',
    'i': 'E5',
    'o': 'F5',
    'p': 'F#5',
    '[': 'G5',
    ']': 'G#5',
    '\\': 'A5',
    '`': 'A#5',
    '1': 'B5',
    '2': 'C6',
    '3': 'C#6',
    '4': 'D6',
    '5': 'D#6',
    '6': 'E6',
    '7': 'F6',
    '8': 'F#6',
    '9': 'G6',
    '0': 'G#6',
    '-': 'A6',
    '=': 'A#6',
    'backspace': 'B6',
    'esc': 'C7',
    'f1': 'C#7',
    'f2': 'D7',
    'f3': 'D#7',
    'f4': 'E7',
    'f5': 'F7',
    'f6': 'F#7',
    'f7': 'G7',
    'f8': 'G#7',
    'f9': 'A7',
    'f10': 'A#7',
    'f11': 'B7',
    'f12': 'C8',
    'print screen': 'A#1',
    'scroll lock': 'B1',
    'insert': 'C2',
    'home': 'C#2',
    'page up': 'D2',
    'delete': 'D#2',
    'end': 'E2',
    'page down': 'F2',
    'up': 'F#2',
    'left': 'G2',
    'down': 'G#2',
    'right': 'A2',
    'num 0': 'C5',
    'decimal': 'C#5',
    'num 1': 'D5',
    'num 2': 'D#5',
    'num 3': 'E5',
    'num 4': 'F5',
    'num 5': 'F#5',
    'num 6': 'G5',
    'num 7': 'G#5',
    'num 8': 'A5',
    'num 9': 'A#5',
    'num /': 'B5',
    '*': 'C6',
    'num -': 'C#6',
    'plus': 'D6',
    'enter2': 'D#6'
}

reverse_key_settings = {j: i for i, j in key_settings.items()}

# switching mode for self playing ('self'),
# or play midi ('show'),
# or play chords with self-configured playing chords keys settings ('chord')
mode = 'show'
self_device = 'pc'
#self_device = 'midi keyboard'
midi_device_id = 1

# operation key settings for pause, unpause, repeat and so on
pause_key = 'space'
repeat_key = 'ctrl'
unpause_key = 'enter'
exit_key = 'esc'
pause_key_clear_notes = False

# show_chord set to True will show what chords you are playing on the screen,
# including what the notes are and the chord's type
show_chord = True

# show_key set to True will show what keyboard keys you are pressing
show_key = False

# if mode is 'show', you can set musicsheet as a musicpy sentence,
# or set the path of midi you want to play
musicsheet = "(chd('C','maj7').set(4,1))*3"

path = r'G:\fl studio files\aaa\mp3和midi文件\midi文件\you2.mid'

# these are the number of tracks of the midi you want to play from
track_ind = 2
track = 1

# the bpm you want to play
bpm = None

# play_interval: play the parts of the midi in this interval (percentages)
play_interval = 0,20

# these are the init parameters of the mixer
frequency = 44100
size = -16
channel = 1
buffer = 1024
maxinum_channels = 100

# global volume of playing, 1 is the maximum and 0 is the minimum
global_volume = 1

# if delay is set to True, when you are self playing, the sounds will
# last for delay_time seconds
delay = True
delay_time = 3

# touch interval is when the sound is still on delay, if you re-press
# the key for the same key for that sound, the time interval between
# the last time you press the key and this time is beyond this interval,
# then the sound will stop and replay again, this paramter is used
# for pressing keys' sensitivity.
touch_interval = 0.1

# this parameter is set to True, if the show_chord is set to True,
# then it only reads the key you are actually pressing now,
# not to include the sounds on delay but you are not pressing
delay_only_read_current = True

# the suffix of the sound files
sound_format = 'wav'

# the path of the sounds folder
sound_path = 'sounds/'

# when the mode is in 'show' mode, the delay time for the sounds
show_delay_time = 1

# this is the tiny time interval at each loop to load and play midi notes,
# better to set around 3 to 10 milliseconds (0.003 to 0.01 seconds)
delay_each_loop = 0.003

# these are the parameters for chord types detections (as you set show_chord to True)
# ignore_sort_from : avoid the detection result are sorting from another chord as much as possible
# change_from_first: detection result is preferentially chosen as changed from another chord(flat or sharp some notes)
# original_first: detection result is preferentially chosen as a variation of the original position of the chord(i.e. no inversion or any changes to the notes of the chord)
# ignore_add_from : detection result will ignore the result for adding notes from another chord
ignore_sort_from = False
change_from_first = True
original_first = True
ignore_add_from = True
same_note_special = False
two_show_interval = True

# the operations on the midi you want to play
# show_change_pitch : a positive number: will sharp all the notes in the midi by the number; a negative number: same except flat all the notes
# show_modulation : [scale1, scale2] perform modulation from scale1 to scale2 on the notes in the midi
show_change_pitch = None
show_modulation = None

# if this is set to True, then you enable the config key during the playing
config_enable = True

# if you press the config key with the following keys, those keys will be able to adjust settings in realtime.
config_key = 'alt'

# volume change keys
volume_up = '='
volume_down = '-'

# volume change of each volume up/down
volume_change_unit = 0.05

# if delay is set to True before you press, then it will change to False, if False before then set to True
change_delay = 'd'
change_read_current = 'c'
change_pause_key_clear_notes = 'x'

# chords types for each key if you use 'chord' mode
# During the chord mode, if you press a root note key with a chord key,
# then the piano will play that chord types with the root note,
# you can set some keys for chord inversions (i.e. 1st inversion, 2nd inversion, ...),
# and you can even set keys for reversing a chord, and the tempo and interval of the
# chord could also be setted and changed.
CHORDKEY = {
    'num 0': 'maj',
    'decimal': 'm',
    'num 1': '7',
    'num 2': 'maj7',
    'num 3': 'm7',
    'num 4': 'dim7',
    'num 5': 'o7',
    'num 6': 'aug',
    'num 7': 'fifth 9th',
    'num 8': '5(+octave)',
    'num 9': 'mM7'
}

# keys for chord inversions and reversing
CHORD_MODIFY = {
    'f1': [1, 'inv'],
    'f2': [2, 'inv'],
    'f3': [3, 'inv'],
    'f4': [4, 'inv'],
    'f5': [0, 'reverse'],
    'f6': [1, 'inv_high']
}

# chords' intervals and durations (timing unit: miliseconds)
chord_interval = 0.3
chord_duration = 1
note_place = [
    (-2, 50), (11, 102), (24, 50), (45.25, 50), (58.25, 102), (71.25, 50),
    (84.25, 102), (97.25, 50), (118.5, 50), (131.5, 102), (144.5, 50),
    (157.5, 102), (170.5, 50), (183.5, 102), (196.5, 50), (217.75, 50),
    (230.75, 102), (243.75, 50), (256.75, 102), (269.75, 50), (291.0, 50),
    (304.0, 102), (317.0, 50), (330.0, 102), (343.0, 50), (356.0, 102),
    (369.0, 50), (390.25, 50), (403.25, 102), (416.25, 50), (429.25, 102),
    (442.25, 50), (463.5, 50), (476.5, 102), (489.5, 50), (502.5, 102),
    (515.5, 50), (528.5, 102), (541.5, 50), (562.75, 50), (575.75, 102),
    (588.75, 50), (601.75, 102), (614.75, 50), (636.0, 50), (649.0, 102),
    (662.0, 50), (675.0, 102), (688.0, 50), (701.0, 102), (714.0, 50),
    (735.25, 50), (748.25, 102), (761.25, 50), (774.25, 102), (787.25, 50),
    (808.5, 50), (821.5, 102), (834.5, 50), (847.5, 102), (860.5, 50),
    (873.5, 102), (886.5, 50), (907.75, 50), (920.75, 102), (933.75, 50),
    (946.75, 102), (959.75, 50), (981.0, 50), (994.0, 102), (1007.0, 50),
    (1020.0, 102), (1033.0, 50), (1046.0, 102), (1059.0, 50), (1080.25, 50),
    (1093.25, 102), (1106.25, 50), (1119.25, 102), (1132.25, 50), (1153.5, 50),
    (1166.5, 102), (1179.5, 50), (1192.5, 102), (1205.5, 50), (1218.5, 102),
    (1231.5, 50), (1252.75, 50)
]
