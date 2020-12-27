user_sec = int(input('Введите колличество секунд - '))
hours = user_sec // 3600
user_sec = user_sec - 3600 * hours
minutes = user_sec // 60
sek = user_sec - 60 * minutes
print(f'{hours}:{minutes}:{sek}')
