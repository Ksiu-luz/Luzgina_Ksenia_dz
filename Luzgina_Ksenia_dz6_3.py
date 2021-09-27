import pickle

result = {}
with open('users.csv', 'r', encoding='utf-8') as users_f, open('hobby.csv', 'r', encoding='utf-8') as hobby_f:
    hobby = hobby_f.readline()
    user = users_f.readline()

    while user:
        user = user.replace('\n', '')
        user = ' '.join(user.split(','))
        if hobby:
            hobby = hobby.replace('\n', '')
            hobby = hobby.split(',')
        else:
            hobby = None
        result[user] = hobby
        user = users_f.readline()
        hobby = hobby_f.readline()

with open('result.csv', 'wb') as f:
    result = pickle.dumps(result)
    f.write(result)

if hobby:
    exit('1')
