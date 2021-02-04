i = 0
user_str = []
while i < 3:
    user = f'{input("Введите строку - ")} \n'
    user_str.append(user)
    i += 1

with open('file_1.txt', 'w') as el:
    el.writelines(user_str)
