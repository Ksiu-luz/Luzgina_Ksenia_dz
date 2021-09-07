my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result_list = []
for i in range(len(my_list)):
    for symb in my_list[i]:
        if symb == '+' or symb == '-':
            my_list[i] = '"' + symb + (str('%02d' % int(my_list[i]))) + '"'
            break
        elif symb in digits:
            my_list[i] = '"' + (str('%02d' % int(my_list[i]))) + '"'
            break
print(' '.join(my_list))
