class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} плавно рисует на листе')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} выводит графичные линии')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} оставляет жирные и яркие следы')


if __name__ == '__main__':
    brush = Stationery('кисть')
    brush.draw()
    pen = Pen('ручка')
    pen.draw()
    pencil = Pencil('карандаш')
    pencil.draw()
    handle = Handle('маркер')
    handle.draw()
