def saberi(lista):

    nova_lista = list(map(sum, lista))

    return nova_lista


def saberi2(lista):

    nova_lista = [sum(x) for x in lista]

    return nova_lista


result1 = saberi([(1, 4, 6), (2, 4), (4, 1)])
result2 = saberi2([(1, 4, 6), (2, 4), (4, 1)])

print(result1, result2)