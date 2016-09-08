#!/usr/bin/env python
from rules import *

# This is coded for clarity, not efficiency.
# Author: Modal(Hex)
# Date..: Monday, June 11th, 2016

initial = input('Enter string\n')
caesar_cipher = ''

for char in initial.lower():
    if SHIFT_DIRECTION == 'LEFT':
        try:
            shifted_char = CHARSET[CHARSET.index(char) - SHIFT_AMOUNT]
        except IndexError:
            shifted_char = wrap_list(char)
    elif SHIFT_DIRECTION == 'RIGHT':
        try:
            shifted_char = CHARSET[CHARSET.index(char) + SHIFT_AMOUNT]
        except IndexError:
            shifted_char = wrap_list(char)
    caesar_cipher += shifted_char
print(caesar_cipher)
