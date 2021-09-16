import requests


def currency_rates(user_name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

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
                name = char[0]
                result_list.append(name)
        rates = line.split('<Value>')
        for rate in rates:
            if '</Value>' in rate:
                rate = rate.split('</')
                value = rate[0]
                result_list.append(value)
        value_list.append(result_list)
        result_list = []
    for list in value_list:
        value_dict[list[0]] = list[1]
    print(value_dict)
    print(value_dict[user_name])


if __name__ == '__main__':
    currency_rates('AUD')
