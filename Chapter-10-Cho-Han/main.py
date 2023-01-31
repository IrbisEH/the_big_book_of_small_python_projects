import random, sys

JAPANES_NUMBERS = {
    1: 'CHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

purse = 5000

while True:
    print(f'You have, {purse} mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter the number')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)


    print('Decide "CHO" (even) or "HAN" (odd).')

    while True:
        bet = input('> ')
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print(f'  {JAPANES_NUMBERS[dice1]} - {JAPANES_NUMBERS[dice2]}')
    print(f'    {dice1} - {dice2}')

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print(f'You won! You take {pot} mon.')
        purse += pot
    else:
        purse -= pot
        print('You lost!')

    if purse == 0:
        sys.exit()