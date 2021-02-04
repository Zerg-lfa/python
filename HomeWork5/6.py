data = {}
with open('file_6.txt', 'r', encoding='utf-8') as el:
    for line in el:
        content = line.split()
        key = content[0].strip(':')
        total = 0
        for elem in content:
            num = '0'
            for i in elem:
                if i.isdigit():
                    num += i
            total += int(num)

        data[key] = total
print(data)




