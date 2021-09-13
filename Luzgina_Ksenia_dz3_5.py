import random


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    joke_list = []

    for i in range(number):
        joke.append(random.choice(nouns))
        joke.append(random.choice(adverbs))
        joke.append(random.choice(adjectives))
        joke_list.append(' '.join(joke))
        joke = []

    return joke_list


if __name__ == '__main__':
    print(get_jokes(2))
