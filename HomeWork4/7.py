def fact(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        yield factorial


a = int(input('Введите число для вычисления факториала - '))
for el in fact(a):
    print(el)
