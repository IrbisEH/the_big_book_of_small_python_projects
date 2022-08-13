import datetime
import random





def get_birthdays(numbers_of_birthdays):
    """Возращаем список объектов дат для случайных дней рождений."""
    birthdays = []
    for i in range(numbers_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        print(start_of_year, type(start_of_year))
        random_numbers_of_days = datetime.timedelta(random.randint(0, 364))
        print(random_numbers_of_days, type(random_numbers_of_days))
        birthday = start_of_year + random_numbers_of_days
        birthdays.append(birthday)
    return birthdays



get_birthdays(10)