from functools import reduce
from itertools import accumulate
import math


def kreiraj(N):
    tuplovi = []

    for i in range(N + 1):

        zbir = sum(range(i + 1))

        rez = int(math.pow(zbir, 2))

        tuplovi.append((f'{i} ', rez))

    return tuplovi


result = kreiraj(4)
print(result)