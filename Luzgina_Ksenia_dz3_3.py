def thesaurus(*args):
    user_list = args
    names_dict = {}
    for names in user_list:
        if not names[0] in names_dict:
            names_dict[names[0]] = []
            names_dict[names[0]].append(names)
        else:
            names_dict[names[0]].append(names)
    return names_dict


def sorted_dict(user_dict, reverse=False):
    if reverse:
        sorted_list = sorted(user_dict, reverse=True)
    else:
        sorted_list = sorted(user_dict)
    result_dict = {}
    for symbol in sorted_list:
        result_dict[symbol] = user_dict[symbol]
    return result_dict


if __name__ == '__main__':
    users_names = thesaurus('Мария', 'Марина', 'Ульяна', 'Егор')
    print(users_names)
    print(users_names['У'])
    print(sorted_dict(users_names, reverse=True))
