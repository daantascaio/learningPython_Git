# dir, hasattr e getattr em Python

name = 'Caio'
metodo = 'upper'
if hasattr(name, metodo):
    print('Uaaala')
    print(getattr(name, metodo)())
else:
    print('F total')