def zbir(lista):

    nova_lista = [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]

    return nova_lista


def zbir2(lista):

    nova_lista = [x + y for x, y in zip(lista, lista[1:])]

    return nova_lista


result = zbir2([1,2,3,4,5])
print(result)