import math

def stepen(lista):

    final_list = [(int)(math.pow(x, y)) for x,y in zip(lista, lista[1:])]

    print(final_list)


stepen([1, 5, 2, 6, 1, 6, 3, 2, 9])