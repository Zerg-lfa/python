my_list = []
count = 0

while count < 6:
    my_list.append(input('Введите любой эллемент - '))
    count += 1

count = 0
for i in range(int(len(my_list) / 2)):
    my_list[count], my_list[count + 1] = my_list[count + 1], my_list[count]
    count += 2

print(my_list)