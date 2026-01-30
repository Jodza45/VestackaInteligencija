import functools

def izracunaj(lista):

    final_list = [functools.reduce(lambda x, y: x * y, i, initial=1) if type(i).__name__ == 'list' else i for i in lista]

    print(final_list)


izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]])