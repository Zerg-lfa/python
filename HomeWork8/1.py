class Date:
    date = ''

    def __init__(self, date):
        Date.date = date


    @classmethod
    def extraction(cls):
        Date.day = int(cls.date[:2])
        Date.month = int(cls.date[3:5])
        Date.year = int(cls.date[6:10])
        print(f'день - {Date.day} \nмесяц - {Date.month} \nгод - {Date.year}')


    @staticmethod
    def validation():
        if Date.date[:2].isdigit() and int(Date.date[:2]) > 0 and int(Date.date[:2]) < 31:
            print('Валидация дня пройдена')
        else:
            print('Введен не корректный день.')

        if Date.date[3:5].isdigit() and int(Date.date[3:5]) > 0 and int(Date.date[3:5]) < 12:
            print('Валидация месяца пройдена')
        else:
            print('Введен не корректный месяц.')

        if Date.date[6:10].isdigit() and int(Date.date[6:10]) > 1900 and int(Date.date[3:5]) < 2021:
            print('Валидация года пройдена')
        else:
            print('Введен не корректный месяц.')



m = Date('11-13-1998')
m.extraction()
m.validation()