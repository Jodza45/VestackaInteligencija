from itertools import zip_longest

def spoji(lista1, lista2):
    final_list = [(min(x,y), max(x,y), x + y) for x, y in zip_longest(lista1, lista2, fillvalue=0)]
    print(final_list)

spoji([1, 7, 2, 4], [2, 5, 2])