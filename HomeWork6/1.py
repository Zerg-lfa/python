from time import sleep

class TrafficLight:
    __color = ' '

    def running(self):
        TrafficLight.__color = 'red'
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = 'green'
        print(TrafficLight.__color)
        time.sleep(5)


obj = TrafficLight()
obj.running()