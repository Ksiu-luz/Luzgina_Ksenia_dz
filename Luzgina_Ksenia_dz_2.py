def sum_seven(user_list):
    sum_in_number = 0
    sum_numbers = 0
    for number in range(len(user_list)):
        str_number = str(user_list[number])
        for i in range(len(str_number)):
            sum_in_number += i
            if sum_in_number % 7 == 0:
                sum_in_number = 0
                sum_numbers += number
    return sum_numbers


if __name__ == '__main__':

    result = []

    for number in range(1, 1001):
        if number % 2 != 0:
            result.append(number ** 3)

    print(sum_seven(result))
    print(sum_seven([x+17 for x in result]))
