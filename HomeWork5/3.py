with open('file_3.txt', 'r', encoding='utf-8') as el:
    content = el.readlines()
    minim = []
    average = 0
    for employee in content:
        i = employee.split()
        if i[1] <= '20000':
            minim.append(employee)
            cash = int(i[1])
            average += cash

        else:
            cash = int(i[1])
            average += cash

print(minim)
print(f'Средняя зп - {average / len(content)}')

