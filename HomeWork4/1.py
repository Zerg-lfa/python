def salary (hour, rate, prize):
    if hour > 0 and rate > 0 and prize >= 0:
        return (hour * rate) + prize
    else:
        print('Не корректный ввод')


print("з/п = ", salary(int(input('Введите кол-во часов - ')), int(input('Введите ставку за час - ')), int(input('Введите премию - '))))