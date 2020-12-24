user_num = int(input('Введите любое положительное число - '))
num = 0
while user_num > 0:
    x = user_num % 10
    user_num = user_num // 10
    if x > num:
        num = x
        user_num = user_num // 10

print(num)
