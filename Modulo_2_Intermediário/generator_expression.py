import sys


# Generator expression, Iterables e Iterantors em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(10000)]
generetor = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generetor))

