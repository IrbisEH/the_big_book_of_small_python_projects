"""Имитационное моделирование парадокса дней рождений"""


import datetime
import random


def get_birthdays(numbers_of_birthdays):
    """Возращаем список объектов дат для случайных дней рождений."""
    birthdays = []
    for i in range(numbers_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_numbers_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_numbers_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Возвращаем объект даты дня рождения встречающегося
    несколько раз в списке дней рождений."""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a


print('''Парадокс дней рожденений.
Этот парадокс показывает нам что в группе из N человек шансы
что у двух из них одинаковые дни рождения достаточно велики.
Это программа - метод Монте Карло (группа численных методов
для изучения случайных процессов).''')


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('Сколько дней рождений сгенерировать? (Макс 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

print('Генератор генерит...\n')
print('Сгенерированно - {} дней рождений'.format(num_bdays))
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('В этой симуляции, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print('Одинаковые дни рождения - ', date_text)
else:
    print('Нет одинаковых дней рождений')
print()

print('Генерируем', num_bdays, 'случайных дней рождений 100,000 раз')
input('Нажми Enter что бы начать')

sim_match = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'симуляция продолжается....')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1

probability = round(sim_match / 100_000 * 100, 2)
print('Вероятность что есть  одинаковые дни рождения - {} %'.format(probability))


