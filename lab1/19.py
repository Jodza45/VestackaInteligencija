from functools import reduce
import math


def stepenuj(lista):
    rez = []

    for x in lista:
        if len(x) > 1:
            element = reduce(lambda x, y: math.pow(x, y), x)
            rez.append(int(element))
        else:
            rez.append(x[0])

    return rez


result = stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )])
print(result)