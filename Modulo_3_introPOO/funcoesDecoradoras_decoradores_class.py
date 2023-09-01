# Funções decoradoras e decoradores com classes 

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__                        HERANÇA DESNECESSÁRIA
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
    

@adiciona_repr  #                                           MANEIRA SIMPLES E MAIS INDICADA
class Time:
    def __init__(self, nome):
        self.nome = nome

    # def __repr__(self) -> str:
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'        REPETE CÓDIGO
    #     return class_repr

@adiciona_repr  #                                           MANEIRA SIMPLES E MAIS INDICADA
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    # def __repr__(self) -> str:
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'        REPETE CÓDIGO
    #     return class_repr

# adiciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

# adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)