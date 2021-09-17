import requests


def currency_rates(char_name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    char_name = char_name.upper()

    response = requests.get(url)
    result = response.text.split('><Valute ID')
    result_list = []
    value_list = []
    value_dict = {}

    for line in result:
        if 'encoding' in line:
            continue
        chars = line.split('<CharCode>')
        for char in chars:
            if '</CharCode>' in char:
                char = char.split('</')
                result_list.append(char[0])
        rates = line.split('<Value>')
        for rate in rates:
            if '</Value>' in rate:
                rate = rate.split('</')
                value = float(rate[0].replace(',', '.'))
                result_list.append(value)
        value_list.append(result_list)
        result_list = []

    for line in value_list:
        value_dict[line[0]] = line[-1]

    if char_name in value_dict:
        return value_dict[char_name]