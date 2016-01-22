__author__ = 'KoicsD'
from random import randint


tomb = [1,2,3,45,5,6,74,8,9]


def shuffle(elements):
    for i in range(len(elements)):
        s = elements[i]
        rand_number = randint(0, len(elements) - 1)
        elements[i] = elements[rand_number]
        elements[rand_number] = s
    return elements


def organize(elements, sub_list_size):
    result = [[] for i in range(len(elements) // sub_list_size)]
    for i in range(len(elements)):
        result[i % len(result)].append(elements[i])
    return result


tomb = shuffle(tomb)
print(organize(tomb, 4))
