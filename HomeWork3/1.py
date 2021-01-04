def division (a, b):
    if a == 0 or b == 0:
        print('делить на ноль нельзя :(')
        return
    print(a / b)

division(int(input('Введите число - ')), int(input('Введите число - ')))