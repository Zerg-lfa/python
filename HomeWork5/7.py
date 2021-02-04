import json

final =[]
firms = {}
average_final = {}
average = []

with open('file_7.txt', 'r', encoding='utf-8') as file:
    summa = 0
    for line in file:
        content = line.split()
        key = content[0]
        income = (f'{int(content[2]) - int(content[3])}')
        firms[key] = income
        if income > '0':
            average.append(income)
    final.append(firms)
    for summ in average:
        summa += int(summ)
    average_final['average_final'] = summa
    final.append(average_final)

with open('file_7.json', 'w') as file_js:
    json.dump(final, file_js)