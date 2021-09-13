import random


def get_jokes(number, *, uniqueness=False):
    """
    The function generates from one to five jokes.
    :param number: generates the required number of jokes
    :param uniqueness: allows (False) or prohibits (True) repetition of words in jokes
    :return: set number of jokes
    """
    if number > 5:
        number = 5

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    result_list = []

    if uniqueness:
        for i in range(number):
            joke = random.choice(nouns)
            nouns.remove(joke)
            joke_list.append(joke)
            joke = random.choice(adverbs)
            adverbs.remove(joke)
            joke_list.append(joke)
            joke = random.choice(adjectives)
            adjectives.remove(joke)
            joke_list.append(joke)
            result_list.append(' '.join(joke_list))
            joke_list = []
    else:
        for i in range(number):
            joke_list.append(random.choice(nouns))
            joke_list.append(random.choice(adverbs))
            joke_list.append(random.choice(adjectives))
            result_list.append(' '.join(joke_list))
            joke_list = []

    return result_list


if __name__ == '__main__':
    print(get_jokes(4, uniqueness=True))
    print(get_jokes(4, uniqueness=False))
    print(get_jokes(4))
