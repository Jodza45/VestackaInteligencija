import itertools

def objedini(lista1, lista2):
    
    final_list = [(min(x, y), max(x, y)) for x, y in itertools.zip_longest(lista1, lista2, fillvalue=0)]
    print(final_list)


objedini([1, 7, 2, 4, 5], [2, 5, 2])