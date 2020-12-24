profit = int(input('Введите прибыль вашей фирмы - '))
costs = int(input('Введите издержки вашей фирмы - '))

if profit > costs:
    cash = profit - costs
    print(f'Ваша прибыль состовляет {cash}')
    print(f'Соотношение прибыли к убыткам {costs / profit * 100}%')
    staff = int(input('Введите количество ваших сотрудников - '))
    print(f'Ваша прибыль на сотрудника состовляет {cash // staff}')
else:
    print('Вы работаете в минус :(')