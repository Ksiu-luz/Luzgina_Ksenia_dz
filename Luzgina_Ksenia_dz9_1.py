from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('red', 5), ('yellow', 2), ('green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(f'!{color}! Wait {sec} sec.')
            sleep(sec)


if __name__ == '__main__':

    traffic_light = TrafficLight()
    traffic_light.running()
