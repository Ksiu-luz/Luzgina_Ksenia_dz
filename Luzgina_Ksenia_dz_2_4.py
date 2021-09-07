my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(my_list)):
    phrase = my_list[i]
    phrase = phrase.split(' ')
    print(f'Привет {phrase[-1].title()}!')
