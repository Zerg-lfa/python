class Check(Exception):
    def __init__(self, param):
        self.param = param


numbers = []
power = True
while power:
    user_input = input('Введите любое число. для выхода из цикла напишите "stop" -  ')
    try:
        if user_input == 'stop':
            power = False
            print(numbers)
            break
        elif user_input.isdigit():
            user_input = int(user_input)
            numbers.append(user_input)
        else:
            raise Check('Вы ввели не число')
    except Check as err:
        print('Вы ввели не число')
