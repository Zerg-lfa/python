from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name):
        self.name = name

class Coat(Clothes):

    def __init__(self, name,  V):
        Clothes.__init__(self, name='clothes')
        self.V = V


    @property
    def math(self):
        return f'{self.V/6.5 + 0.5}'


class Costume(Clothes):

    def __init__(self, name,  H):
        Clothes.__init__(self, name='clothes')
        self.H = H

    @property
    def math(self):
        return f'{2 * self.H + 0.3}'



a = Coat('DG', 30)

b = Costume('LV', 1.90)



print(f'{float(a.math) + float(b.math)}')