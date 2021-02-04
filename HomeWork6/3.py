cash = {"wage": 50000, "bonus": 20000}

class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'engineer'
    _income = cash

class Position(Worker):

    def get_full_name(self):
        print(Worker.name)

    def get_total_income(self):
        print(f'Общий доход - {Worker._income["wage"] + Worker._income["bonus"]}р.')


obj = Position()

obj.get_full_name()
obj.get_total_income()