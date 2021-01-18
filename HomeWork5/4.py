words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as el:
    for string in el:
        line = string.split(' ', 1)
        new_file.append(f'{words[line[0]]} {line[1]}')
        with open('file_4.1.txt', 'w', encoding='utf-8') as el_1:
            el_1.writelines(new_file)

# print(new_file)