user_time = int(input('Введите кол-во секунд: '))
units = {'дн': 86400, 'час': 3600, 'мин': 60, 'сек': 1}
result = []


for key, val in units.items():
    if user_time // int(val) != 0:
        result.append(str(user_time // int(val)))
        result.append(key)
        user_time = user_time % int(val)


print(' '.join(result))