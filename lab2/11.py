import functools

def proizvod(lista):

    final = functools.reduce(lambda x, y: x * y, [functools.reduce(lambda x, y: x * y, i, initial=1) for i in lista])

    print(final)


proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]])