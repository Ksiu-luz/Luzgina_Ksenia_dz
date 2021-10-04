class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is driving')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')


class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name} exceeds the permissible speed')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name} exceeds the permissible speed')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    work_car = WorkCar(50, 'red', 'golf car', False)
    work_car.show_speed()
    work_car.stop()
    town_car = TownCar(50, 'gray', 'kia rio', False)
    town_car.show_speed()
    town_car.go()
    police_car = PoliceCar(80, 'white', 'UAZ Hunter', True)
    police_car.turn('left')
    sport_car = SportCar(500, 'pink', 'Audi S3', False)
    sport_car.show_speed()
