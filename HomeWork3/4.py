def my_func (x, y):
    print(x ** y)
    count = - 1
    result = x

    while count > y:
        result = result * x
        count -= 1

    print(1 / result)


my_func(10, -4)




