#!/usr/bin/env python3
import random
import numpy as np

strings = '''           {19}
        ---{18}---
           {17}
        ---{16}---
           {15}
    -------{14}-------
           {13}
    -------{12}-------
           {11}
    -------{10}-------
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

notesSK = (
    ["ре", 19],
    ["до", 18],
    ["си", 17],
    ["ля", 16],
    ["соль", 15],
    ["фа", 14],
    ["ми", 13],
    ["ре", 12],
    ["до", 11],
    ["си", 10],
    ["ля", 9],
    ["соль", 8],
    ["фа", 7],
    ["ми", 6],
    ["ре", 5],
    ["до", 4],
    ["си", 3],
    ["ля", 2],
    ["соль", 1],
)


def print_notes(note):
    note_pos = np.full((20), ' ')
    note_pos[note[1]] = u'\u266A'

    keys_pos = np.full((8), '')

    for item in notes:
        if item[0] == note[0]:
            keys_pos[item[1]] = '^'

    print(strings.format(*note_pos))
    num = input("")
    note_pos[note[1]] = note[0]
    print(keys.format(*keys_pos))
    if num == note[0]:
        print("\n ====== Верно ==================")
    else:
        print("\n !!!! не '{0}', а '{1}' !!!!!!".format(num, note[0]))


while 1 < 2:
    one = random.choice(notesSK)
    print_notes(one)
