class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} - {self.position}'

    def get_total_income(self):
        return f'Оклад: {self._income["wage"] + self._income["bonus"]} руб.'


if __name__ == '__main__':
    pos = Position('Иван', 'Иванов', 'охранник', 15000, 3000)
    print(pos.get_full_name())
    print(pos.get_total_income())
