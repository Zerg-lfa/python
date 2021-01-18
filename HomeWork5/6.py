data = {}
with open('file_6.txt', 'r', encoding='utf-8') as el:
    for line in el:
       a, b, c, d = line.split()

       data[a] = int(b) + int(c) + int(d)
print(f"Общее кол- во часов по предмету - ")

