def objedinji(lista):
    
    dict = {x[0]: (None if len(x) < 2 else list(x[1:])) for x in lista}
    print(dict)


objedinji([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)])