class Road:

    def payment(self, _width, _length):
        self._width = _width
        self._length = _length
        print(f'Потребуется - {_width * _length * 25 * 5 /1000}т.')


obj = Road()

obj.payment(20, 10000)

# ------------------------------------------------------------------------------
# Не знал как сделать корректно сделал 2 варианта

class Road_1:
    _length = 0
    _width = 0


    def __init__(self, width, length):
        Road_1._width = width
        Road_1._length = length

    def payment(self):
        print(f'Потребуется - {Road_1._width * Road_1._length * 25 * 5 / 1000}т.')

obj_1 = Road_1(20, 10000)
obj_1.payment()