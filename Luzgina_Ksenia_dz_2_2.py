def format_numbers(number):
    return str('%02d' % int(number))


def quotes(user_list, text):
    user_list.append('"')
    user_list.append(text)
    user_list.append('"')
    user_list.append(' ')


if __name__ == '__main__':

    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result_list = []

    for count in range(len(my_list)):
        for symbol in my_list[count]:
            if symbol == '+' or symbol == '-':
                quotes(result_list, symbol + (format_numbers(my_list[count])))
                break
            elif symbol in digits:
                quotes(result_list, format_numbers(my_list[count]))
                break
            else:
                result_list.append(my_list[count])
                result_list.append(' ')
                break

    print(''.join(result_list))
