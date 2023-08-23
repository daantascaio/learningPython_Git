# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções

#   (sem underline) = public
#       pode ser usado em qualquer lugar

# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.

# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial # só mostrando que tem ( _, __ nesse código)

class Foo:
    
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def __metodo_private(self):
        return '__metodo_private'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'

f = Foo()
print(f.public)
print(f.metodo_publico())
print('################')                   
print(f._protected)
print(f._metodo_protected())
print('################')

# print(f.__private)
# print(f.__metodo_privado())

print(f._Foo__private)
print(f._Foo__metodo_private())