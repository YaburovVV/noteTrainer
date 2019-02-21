#!/usr/bin/env python3
import random
import numpy as np
import sys
from enum import Enum


class Clef(Enum):
    g = u'\U0001D11E'
    f = u'\U0001D122'


note_sign = u'\u266A'
key_pointer_sign = '^'
strings = '''           {19}
        ---{18}---
           {17}
        ---{16}---
           {15}
    -------{14}-------
           {13}
    -------{12}-------
           {11}
{0}   -------{10}-------
           {9}
    -------{8}-------
           {7}
    -------{6}-------
           {5}
        ---{4}---
           {3}
        ---{2}---
           {1}'''

keys = '''_____________________________
| |  ||  |  | |  ||  ||  |  |
| |__||__|  | |__||__||__|  |
|   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|
  {1}    {2}    {3}    {4}    {5}    {6}    {7}'''

notes = [
    ["си", 7],
    ["ля", 6],
    ["соль", 5],
    ["фа", 4],
    ["ми", 3],
    ["ре", 2],
    ["до", 1],
]

notesGF = (
    # ["ре", 19, "фа"],
    # ["до", 18, "ми"],
    # ["си", 17, "ре"],
    # ["ля", 16, "до"],
    ["соль", 15, "си"],
    # ["фа", 14, "ля"],
    # ["ми", 13, "соль"],
    # ["ре", 12, "фа"],
    # ["до", 11, "ми"],
    # ["си", 10, "ре"],
    # ["ля", 9, "до"],
    # ["соль", 8, "си"],
    ["фа", 7, "ля"],
    ["ми", 6, "cоль"],
    # ["ре", 5, "фа"],
    # ["до", 4, "ми"],
    # ["си", 3, "ре"],
    ["ля", 2, "до"],
    # ["соль", 1, "си"],
)


def print_notes(note, clef):
    if clef == Clef.g:
        clef_column = 0
    elif clef == Clef.f:
        clef_column = 2
    else:
        sys.exit()

    note_pos = np.full((20), ' ')
    note_pos[0] = clef.value
    note_pos[note[1]] = note_sign

    keys_pos = np.full((8), '')

    for item in notes:
        if item[0] == note[clef_column]:
            keys_pos[item[1]] = key_pointer_sign

    print(strings.format(*note_pos))
    num = input("")
    note_pos[note[1]] = note[0]
    print(keys.format(*keys_pos))
    if num == note[clef_column]:
        print("\n ====== Верно ==================")
    else:
        print("\n !!!! не '{0}', а '{1}' !!!!!!".format(num, note[0]))


while True:
    one = random.choice(notesGF)
    print_notes(one, Clef.g)
