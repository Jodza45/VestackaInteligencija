def izbroj(nesto):

    return sum(izbroj(x) if isinstance(x, list) else 1 for x in nesto)

def izbroj2(nesto):

    if not isinstance(nesto, list):
        return 1
    
    suma = 0
    for x in nesto:
        suma += izbroj2(x)

    return suma


result = izbroj2([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6])
print(result)