from functools import wraps


def val_checker(lambda_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            if lambda_func(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    result = calc_cube(5)
    print(result)
    result = calc_cube(-5)
    print(result)
