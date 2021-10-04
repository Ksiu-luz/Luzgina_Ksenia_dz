class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        mass_m = 25
        thickness = 5
        result_mass = (self._length * self._width * mass_m * thickness) / 10000
        print(f'Потребуется {result_mass} тонн асфальта')


if __name__ == '__main__':
    asphalt = Road(20, 500)
    asphalt.mass_calc()
