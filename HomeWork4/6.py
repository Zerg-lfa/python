from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

i = 0

for el in cycle('12345'):
    print(el)
    if i > 20:
        break
    i += 1
