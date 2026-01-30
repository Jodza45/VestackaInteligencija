# Korišdenjem programskog jezika Python, napisati funkciju suma, koja prvenstveno određuje proizvod
# elemenata u svakoj podlisti unutar prosleđene liste, a zatim sumu tako dobijenih elemenata. Zabranjeno je
# korišdenje petlji (osim u comprehension sintaksi) i funkcije sum i prod.
# Primer: suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = 630

from itertools import *
from functools import *

def suma(lista):

    final_list = reduce(lambda x, y: x + y, [reduce(lambda x, y: x * y, z, initial=1) for z in lista])

    print(final_list)


suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])