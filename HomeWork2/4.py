user = input('Введите несколько слов различной длины, отделяя их проблеом - ')
user = user.split(' ')
print(user)

for ind, el in enumerate(user, 1):
    if int(len(el)) > 10:
        print(ind, el[0: 10])
    else:
        print(ind, el)