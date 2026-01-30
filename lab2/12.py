import math

def izracunaj(lista):

    final_list = [(int)(sum([math.pow(x, 2) for x in y])) if type(y).__name__ == 'list' else (int)(math.pow(y, 2)) for y in lista]

    print(final_list)


izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]])