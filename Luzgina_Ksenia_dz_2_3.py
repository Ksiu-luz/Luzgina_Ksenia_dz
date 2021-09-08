def format_numbers(number):
    return str('%02d' % int(number))


if __name__ == '__main__':

    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    count = 1

    while count <= len(my_list):
        word = my_list[count-1]
        for i in range(len(word)):
            if word[i] == '+' or word[i] == '-':
                my_list[count-1] = word[i] + format_numbers(word)
                my_list.insert(count-1, '"')
                my_list.insert(count+1, '"')
                count += 2
                break
            elif word[i] in digits:
                my_list[count-1] = format_numbers(word)
                my_list.insert(count - 1, '"')
                my_list.insert(count + 1, '"')
                count += 2
                break
            else:
                count += 1
                break
    print(' '.join(my_list))
