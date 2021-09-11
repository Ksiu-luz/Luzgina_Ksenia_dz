def num_translate_adv(num):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два',
               'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть',
               'seven': 'семь', 'eight': 'восемь',
               'nine': 'девять', 'ten': 'десять'}
    for symbol in num:
        if symbol.isupper():
            num = num.lower()
            return numbers[num].title()
        break
    if num in numbers:
        return numbers[num]


if __name__ == '__main__':
    print(num_translate_adv('zero'))
