class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        result = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with the form'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Problems with the form'
        return result


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
    matrix_2 = Matrix([[6, 5], [4, 3], [2, 1]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_4 = Matrix([[1, 2], [3, 4]])

    print(matrix_3)
    print(matrix_1 + matrix_2)
    print(matrix_2 + matrix_3)
    print(matrix_3 + matrix_4)
