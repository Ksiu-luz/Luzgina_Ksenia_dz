user_time = int(input('Введите кол-во секунд: '))
units_of_time = ('дн', 'час', 'мин', 'сек')
seconds_in_units = (86400, 3600, 60, 1)
result = []


for i in range(0, 4):
    if user_time // seconds_in_units[i] != 0:
        result.append(str(user_time // seconds_in_units[i]))
        result.append(units_of_time[i])
        user_time = user_time % seconds_in_units[i]


print(' '.join(result))