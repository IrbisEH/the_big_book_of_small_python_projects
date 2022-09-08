"""Caesar Cipher"""

try:
    import pyperclip
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')