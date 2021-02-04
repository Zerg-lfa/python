from random import randint
inter = []
while len(inter) < 10:
    inter.append(randint(1, 100))


with open('file_5.txt', 'r+', encoding='utf-8') as el:
    print(*inter, file=el)
    content = el.readline()
    content = content.split()
    print(content)
    summ = 0
    for i in content:
        summ += int(i)

print(summ)

