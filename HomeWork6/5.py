class Stationery:
    title = ''
    def __init__(self, title):
        Stationery.title = title


    def draw(self):
        print(f'Запуск отрисовки, {Stationery.title}')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручки')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')

obj1 = Stationery('Канцелярия')
obj1.draw()
obj2 = Pen('Ручка')
obj2.draw()
obj3 = Pencil('Карандаш')
obj3.draw()
obj4 = Handle('Маркер')
obj4.draw()