from rules import *

initial = input('Enter string\n')
decrypted = ''
for char in initial:
    if SHIFT_DIRECTION == 'LEFT':
        try:
            decrypted_char = CHARSET[CHARSET.index(char) + SHIFT_AMOUNT]
        except:
            decrypted_char = wrap_list(char)
    elif SHIFT_DIRECTION == 'RIGHT':
        decrypted_char = CHARSET[CHARSET.index(char) - SHIFT_AMOUNT]
    decrypted += decrypted_char
print(decrypted)
