my_list = [7, 5, 3, 3, 2]

while True:
    num = int(input('Введите число от 1 до 10 . Если хотите выйти из цыкла введите 666. - '))
    if num == 666:
        print('Конец')
        break
    if num <10 and num > 0:
        my_list.append(num)
        my_list.sort()
        my_list.reverse()
        print(my_list)
