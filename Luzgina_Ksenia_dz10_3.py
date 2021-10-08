class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num > other.num:
            return self.num - other.num
        else:
            return 'В первой клетке ячеек меньше или столько же, сколько во второй, вычитание невозможно'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num


if __name__ == '__main__':
    cell_1 = Cell(20)
    cell_2 = Cell(13)
    print(cell_1.make_order(5))

    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_2 - cell_1)
    print(cell_1 * cell_2)
    print(cell_1 / cell_2)
