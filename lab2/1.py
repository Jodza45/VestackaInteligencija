def poredak(lista1, lista2):
    N = None
    if len(lista1) > len(lista2):
        N = len(lista1) - len(lista2)
        lista2 += [0] * N
    else:
        N = len(lista2) - len(lista1)
        lista1 += [0] * N

    lista_parova = [(x, y, "JESTE" if y == x*2 else "NIJE") for x, y in zip(lista1, lista2)]

    print(lista_parova)


poredak([1, 7, 2, 4], [2, 5, 2])
