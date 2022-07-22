"""Бейглз"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Бейглз - дедуктивно-логическая игра.
Программа загадывает {} цифры без повторов.
Попробуй отгадать какое. Вот некоторые подсказки:
Если на экране:         Это значит:
    
    Pico                Одно число правильное но не на той позиции
    Fermi               Одно число правильное и на правильной позиции
    Bagels              Нет ни одного правильного числа
        
Например, если программа загадала число 248 а твоя догадка была 843,
то подсказка была бы Fermi Pico.\n'''.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print('Программа загадала число.')
        print('У тебя {} попыток отгадать число.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Догадка #{}: '.format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('Попытки закончились')
                print('Число было - {}.'.format(secret_num))

        print('Поиграем еще? (да/нет)')
        if not input('> ').lower().startswith('д'):
            break

    print('Спасибо за игру')


def get_secret_num():
    """Возращает строку из NUM_DIGITS уникальных случайных цифрю"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    return secret_num


def get_clues(guess, secret_num):
    """Возращает строку с подсказками pico, fermi, bagels."""
    if guess == secret_num:
        return 'Ты угадал'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # правильная цифра на неправильном месте
            clues.append('Pico')

    if len(clues) == 0:
        # правильных цифр нет вообще
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
