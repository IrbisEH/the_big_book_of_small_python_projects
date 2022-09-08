"""Caesar Cipher"""

try:
    import pyperclip
except ImportError:
    # If pyperclip is not installed, do nothing. It's no big deal
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MODE = None
KEY = None
MAX_KEY = None
NUM = None

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        MODE = 'encrypt'
        break
    elif response.startswith('d'):
        MODE = 'decrypt'
        break
    print('Please enter the letter e or d')

while True:
    MAX_KEY = len(SYMBOLS) - 1
    print('Please enter the key (0 to {} to use).'.format(MAX_KEY))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        KEY = int(response)
        break

print('Enter the message to {}.'.format(MODE))
message = input('> ').upper()

translated = ''

for char in message:
    if char in SYMBOLS:
        NUM = SYMBOLS.find(char)
        if MODE == 'encrypt':
            NUM = NUM + KEY
        elif MODE == 'decrypt':
            NUM = NUM - KEY
        if NUM >= len(SYMBOLS):
            NUM = NUM - len(SYMBOLS)
        elif NUM < 0:
            NUM = NUM + len(SYMBOLS)

        translated = translated + SYMBOLS[NUM]
    else:
        translated = translated + char

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    # Do nothing if pyperclip wasn't installed.
    pass
