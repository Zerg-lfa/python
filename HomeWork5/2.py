with open('file_2.txt', 'r') as el:
    content = el.readlines()
    count = 1
    for i in content:
        print(f'строка - {count} слов - {len(i.split())}')
        count += 1





