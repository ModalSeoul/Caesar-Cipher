CHARSET = [
    'a', 'b', 'c',
    'd', 'e', 'f',
    'g', 'h', 'i',
    'j', 'k', 'l',
    'm', 'n', 'o',
    'p', 'q', 'r',
    's', 't', 'u',
    'v', 'w', 'x',
    'y', 'z', ' ',
    ',', '.', '?',
    '!', '=', '#',
    '@', '$', '%',
]
SHIFT_DIRECTION = 'RIGHT'
SHIFT_AMOUNT = 20


def wrap_list(char):
    if SHIFT_DIRECTION == 'LEFT':
        safe_index = CHARSET.index(char) - SHIFT_AMOUNT
    elif SHIFT_DIRECTION == 'RIGHT':
        safe_index = CHARSET.index(char) + SHIFT_AMOUNT
    return CHARSET[safe_index % len(CHARSET)]
