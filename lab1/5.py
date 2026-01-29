def brojel(*liste):

    nova_lista = []

    for x in liste:
        if (type(x)).__name__ == "list":
            nova_lista.append(len(x))
        else:
            nova_lista.append(-1)

    return nova_lista


def brojel2(*liste):

    nova_lista = [len(x) if isinstance(x, list) else -1 for x in liste]

    return nova_lista



result = brojel2([1, 2], [3, 4, 5], 'el', ['1', 1])
print(result)