class OwnError(Exception):
    def __init__(self, error):
        self.error = error



a = input('Введитель делимое - ')
b = input('Введите делитель - ')


try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnError('На ноль делить нельзя')
except OwnError as err:
    print(err)
except ValueError:
    print("Вы ввели не число")

print(f'{a / b}')