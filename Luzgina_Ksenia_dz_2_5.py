def price_format(price):
    return '%02d' % (price // 1) + ' руб ' + '%02d' % (price * 100 - (price // 1) * 100) + ' коп'


if __name__ == '__main__':
    prices = [57.8, 46.51, 97, 13.07, 55.16, 6.3, 5.06, 90, 23.12, 10]

    print('корректный список цен: ')

    correct_prices = []
    for price in prices:
        correct_prices.append(price_format(price))
    print(', '.join(correct_prices))
    print(id(correct_prices))

    print('список цен по возрастанию: ')

    correct_prices.sort()
    print(correct_prices)
    print(id(correct_prices))

    print('список цен по убыванию: ')

    max_prices = []
    for price in sorted(prices, reverse=True):
        max_prices.append(price_format(price))
    print(max_prices)

    print('пять самых высоких цен: ')

    print(max_prices[:5])
