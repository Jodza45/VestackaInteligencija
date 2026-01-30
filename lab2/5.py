import functools
import itertools

def proizvod(lista1, lista2):

    #pom = [x for x in [functools.reduce(lambda i, j: i + j, y) for y in lista1]]
    #print(pom)

    #zippom = list(zip(pom, lista2))
   # print(zippom)

    rez = [x*y for x,y in list(zip([x for x in [functools.reduce(lambda i, j: i + j, y) for y in lista1]], lista2))]
    print(rez)



proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3])