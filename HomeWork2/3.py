month = int(input('Введите цифрой номер месяца - '))
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

while True:
    if month > 0 and month <= 12:
        print(f'Вы выбрали месяц {months[month - 1]} , это {season[month - 1]}.')
        break
    else:
        month = int(input('Введите цифрой номер месяца - '))


year = {
    'январь': 'зима',
    'февраль': 'зима',
    'март': 'весна',
    'апрель': 'весна',
    'май': 'весна',
    'июнь': 'лето',
    'июль': 'лето',
    'август': 'лето',
    'сентябрь': 'осень',
    'октябрь': 'осень',
    'ноябрь': 'осень',
    'декабрь': 'зима',
}

my_list = list(year.keys())


while True:
    if month > 0 and month <= 12:
        print(f'Вы выбрали месяц {my_list[month - 1]} , это {year[my_list[month - 1]]}.')
        break
    else:
        month = int(input('Введите цифрой номер месяца - '))