from functools import reduce

b = [el for el in range(100, 1001) if el % 2 == 0]
print(b)


def summ(a, b):
    return a + b


print(reduce(summ, b))
