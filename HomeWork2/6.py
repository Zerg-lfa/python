items = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт'})
]
count = 4

new = (count, {'название': '', 'цена': '', 'количество': '', 'ед': 'шт'})
count += 1
for keys in list(new[1].keys()):
    new[1][keys] = input('Введите поочереди название товара, цена, кол-во и ед.измерения. - ')

items.append(new)
print(items)

# for el in items: