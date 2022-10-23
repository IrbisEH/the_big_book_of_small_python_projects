import random


input('Press Enter to begin...')

p1Name = input('Player 1, enter your name: ')
p2Name = input('Player 2, enter your name: ')
playersNames = p1Name[:11].center(11) + '     ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playersNames)
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
print()
print(p1Name + ', you will ger to look into your box.')
print(p2Name.upper() + ', close yours eyes and don\'t look!')
input('When ' + p2Name + ' has closed thert eyes, press Enter...')
print()
print(p1Name + ' here is the insede of your box:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
       ___VV____
      |   VV    |
      |   VV    |
      |___||____|     __________
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
      (carrot!)''')
    print(playersNames)
else:
    print('''
       _________
      |         |
      |         |
      |_________|     __________
     /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (no carrot!)''')

input('Press enter to continue...')

print('\n' * 100)
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue...')

print()
print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', please enter "YES" or "NO".')
    else:
        break

firstBox = 'RED '
secondBox = 'GOLD '

if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playersNames)

input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
    print('''
       ___VV____
      |   VV    |
      |   VV    |
      |___||____|     __________
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {} | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
      (carrot!)'''.format(firstBox, secondBox))
else:
    print('''
                      ___VV____
                     |   VV    |
                     |   VV    |
      __________     |___||____|
     /         /|   /    ||   /|
    +---------+ |  +---------+ |
    |   {} | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
      (carrot!)'''.format(firstBox, secondBox))

print(playersNames)

if carrotInFirstBox:
    print(p1Name + ' is the winner!')
else:
    print(p2Name + ' is the winner!')

print('Thanks for playing!')


