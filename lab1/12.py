def presek(lista1, lista2):

    novi1 = set(lista1)
    novi2 = set(lista2)

    return list(novi1 & novi2)


def presek2(lista1, lista2):

    nova = []

    for x in lista1:
        if x in lista2:
            nova.append(x)

    return nova




result = presek2([5, 4, "1", "8", 3, 7], [1, 9, "1", 4])
print(result)