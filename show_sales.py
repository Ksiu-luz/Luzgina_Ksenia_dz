import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    i = 0
    if len(sys.argv) == 3:
        start = sys.argv[1]
        end = sys.argv[2]
        for line in f:
            i += 1
            if i >= int(start) and i <= int(end):
                result = line.replace('\n', '')
                print(result)
    elif len(sys.argv) == 2:
        start = sys.argv[1]
        for line in f:
            i += 1
            if i >= int(start):
                result = line.replace('\n', '')
                print(result)
    else:
        print(f.read())
