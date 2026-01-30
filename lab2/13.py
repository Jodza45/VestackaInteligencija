from itertools import *
from functools import *

def skupi(lista):

    final_lista = [[x + y for x, y in zip_longest(l1, l2, fillvalue=0)] for l1, l2 in zip(lista, lista[1:])]
    print(final_lista)
    


skupi([[1, 3, 5], [2, 4, 6], [1, 2]])