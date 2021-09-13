def thesaurus_adv(*args):
    user_list = args
    result_dict = {}
    names_dict = {}

    for full_names in user_list:
        first_name = full_names.split(' ')
        first_name = first_name[-1]
        if not first_name[0] in result_dict:
            result_dict[first_name[0]] = []
            result_dict[first_name[0]].append(full_names)
        else:
            result_dict[first_name[0]].append(full_names)

    for key in result_dict.keys():
        user_names = result_dict[key]
        for user in user_names:
            if not user[0] in names_dict:
                names_dict[user[0]] = []
                names_dict[user[0]].append(user)
            else:
                names_dict[user[0]].append(user)
            result_dict[key] = names_dict
        names_dict = {}

    return result_dict


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
    users_full_names = thesaurus_adv('Виктор Березников', 'Алья Борова',
                                     'Карина Акентьева', 'Виктор Панин', 'Марина Кудрявцева')
    print(users_full_names)
    print(sorted_dict(users_full_names))
    print(sorted_dict(users_full_names['Б']))
