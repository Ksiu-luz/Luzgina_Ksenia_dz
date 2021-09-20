def odd_nums(max_num):
    for number in range(1, max_num + 1, 2):
        yield number


if __name__ == '__main__':

    numbers = odd_nums(15)
    print(*numbers)
    numbers = odd_nums(8)
    print(next(numbers), next(numbers), next(numbers), next(numbers))
    try:
        print(next(numbers))
    except:
        print('герератор закончился')
