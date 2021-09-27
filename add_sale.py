import sys

sale = str(sys.argv[1]) + '\n'
with open('bakery.csv', 'a', encoding='utf-8') as f:

    f.write(sale)
    