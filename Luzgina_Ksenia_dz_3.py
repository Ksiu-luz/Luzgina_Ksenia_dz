percent = input('введите кол-во процентов: ')
exceptions = ['11', '12', '13', '14']
if percent in exceptions:
    print(percent + ' процентов')
elif percent[-1] == '1':
    print(percent + ' процент')
elif percent[-1] == '2' or percent[-1] == '3' or percent[-1] == '4':
    print(percent + ' процента')
else:
    print(percent + ' процентов')
