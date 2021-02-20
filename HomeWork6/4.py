class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    car_status = 'stop'

    def __init__(self, speed, color, name,):
        Car.speed = speed
        Car.color = color
        Car.name = name



    def go(self):
        Car.car_status = 'start'
        print(Car.car_status)

    def stop(self):
        Car.car_status = 'stop'
        print(Car.car_status)

    def turn(self, direction):
            if direction == 'right':
                print('Машина повернула направо')
            elif direction == 'left':
                print('Машина повернула налево')
            else:
                print('ничего не понятно, машина разбилась')

    def show_speed(self):
        print(f'Ваша скорость {Car.speed} км\ч')

class TownCar(Car):

    def show_speed(self):
        if TownCar.speed > 60:
            print(f'Привышеение скорости, немедленно сбрость скорость на {TownCar.speed - 60} км/ч')

class SportCar(Car):

    def show_speed(self):
        if SportCar.speed < 150:
            print(f'Почему мы так медленно едем ?!!!!')

class WorkCar(Car):

    def show_speed(self):
        if WorkCar.speed > 40:
            print(f'Привышеение скорости, немедленно сбрость скорость на {WorkCar.speed - 40} км/ч')

class PoliceCar(Car):
    is_police = True



auto = Car(100, 'red', 'lada')
auto.go()
auto.stop()
auto.turn('rig')
auto.show_speed()


town_auto = TownCar(100, 'red', 'lada')
town_auto.go()
town_auto.stop()
town_auto.turn('rig')
town_auto.show_speed()

sport_Car = SportCar(320, 'blue', 'ferrari')
sport_Car.go()
sport_Car.stop()
sport_Car.turn('right')
sport_Car.show_speed()


work_car = WorkCar(100, 'red', 'lada')
work_car.go()
work_car.stop()
work_car.turn('rig')
work_car.show_speed()