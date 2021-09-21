tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    [klasses.append(None) for i in range(len(tutors) - len(klasses))]
    klasses = tuple(klasses)

result = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(type(result))
while result:
    print(next(result))
