"""___Collatz sequence___"""
"""https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0_%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D1%82%D1%86%D0%B0"""
import sys
import time


print('Input a starting number (greater then 0) or QUIT')

response = input('> ')

if not response.isdecimal() or response == 0:
    print('You must input integer!')
    sys.exit()

n = int(response)
print(n, end='', flush=True)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()