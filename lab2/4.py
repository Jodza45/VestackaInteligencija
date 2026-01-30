import itertools
import functools

def suma(lista):
    
    rez = functools.reduce(lambda x, y: x + y, [functools.reduce(lambda i, j: i + j, z) for z in lista])
    print(rez)


suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])