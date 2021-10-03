import re

EMAIL = re.compile(r'(^[a-zA-Z0-9][a-zA-Z0-9._-]+)@([a-z]+\.[a-z]+)')


def email_parse(email):
    result = {}
    found_info = EMAIL.findall(email)
    if found_info:
        result['username'] = found_info[0][0]
        result['domain'] = found_info[0][-1]
    else:
        raise ValueError(f'wrong email: {email}')
    return result


if __name__ == '__main__':
    print(email_parse('luzgina@mail.ru'))
    print(email_parse('Luzgina-ks3241@gmail.com'))
    print(email_parse('luz@yandexru'))
