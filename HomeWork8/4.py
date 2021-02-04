from sys import exit

class WareHouse:

    def __init__(self, size, places):
        self.size = size
        self.places = places
        self.status = 'closed'
        self.product = []

    def __str__(self):
        return f'Склад'

    def openWareHouse(self):
        self.status = 'open'
        print('Склад открыт')

    def closedWareHouse(self):
        self.status = 'close'
        print('Склад закрыт')


    def sendToStore(self):
        self.product.clear()
        print('Весь товра отправлен в магазин')

class PrintersHouse(WareHouse):



    def __init__(self, size, places):
        WareHouse.__init__(self, size, places)



    def takePrinters(self, *printers):
        for printer in printers:

            self.product.append(printer.printers)


class XeroxHouse(WareHouse):
    def __init__(self, size, places):
        WareHouse.__init__(self, size, places)


    def takeXerox(self, *xerox):
        for i in xerox:
            self.product.append(i.xerox)


class ScannerHouse(WareHouse):
    def __init__(self, size, places, scanner):
        WareHouse.__init__(self, size, places)

    def takeScenner(self, *scanner):
        for i in scanner:
            self.product.append(i.scanner)

class Equipment:
    def __init__(self, manufacturer, quantity):
        try:
            if quantity.isdigit and quantity > '0':
                self.quantity = int(quantity)
            else:
                raise ValueError

        except ValueError:
            print('Введенно не число, программа завершена.')
            exit()

        self.manufacturer = manufacturer


class PrintersEquipment(Equipment):
    printers = {}

    def __init__(self, manufacturer, quantity, printSpeed):
        Equipment.__init__(self, manufacturer, quantity)
        self.printSpeed = printSpeed
        self.printers = {manufacturer: (quantity, printSpeed)}




class XeroxEquipment(Equipment):
    xerox = {}

    def __init__(self, manufacturer, quantity, assembly):
        Equipment.__init__(self, manufacturer, quantity)
        self.assembly = assembly
        self.xerox = {manufacturer: (quantity, assembly)}




a = PrintersHouse(1000, 5000)
samsung = PrintersEquipment('Samsung', input('Сколько принтеров необходимо создать - '), 10)
hp = PrintersEquipment('hp', input('Сколько принтеров необходимо создать - '), 7)
a.takePrinters(samsung, hp)
print(a.product)
a.sendToStore()
print(a.product)


b = XeroxHouse(1000, 5000)
xer = XeroxEquipment('xerox', input('Сколько принтеров необходимо создать - '), 'Germany')
xer2 = XeroxEquipment('xerox', input('Сколько принтеров необходимо создать - '), 'China')
b.takeXerox(xer, xer2)
print(b.product)
b.sendToStore()
print(b.product)