def prosek(lista):

    return [sum(x) / len(x) for x in lista]


result = prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]])
print(result)