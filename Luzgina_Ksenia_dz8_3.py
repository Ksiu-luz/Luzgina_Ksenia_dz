from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f"{arg}: {type(arg)}", end=', ')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


if __name__ == '__main__':
    a = calc_cube(4, 4, 5)
    print(a)
    print(calc_cube.__name__)
