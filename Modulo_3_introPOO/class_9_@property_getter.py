# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo 🤯 🤯 🤯

# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Código cliente - é o código que usa seu código




"""
    AGORA É O MODO PYTHÔNICO
"""

class Caneta:

    def __init__(self, cor, tampa_cor):
        self.cor_tinta = cor
        self.tampa_cor = tampa_cor

    @property
    def cor(self):
        print(2 + 5)
        return self.cor_tinta
    
    @property
    def tampa(self):    
        return self.tampa_cor

caneta = Caneta('Azul', 'Vermelha')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print()
print(caneta.tampa)
print(caneta.tampa)
print(caneta.tampa)
print(caneta.tampa)


###################################################################


# class Caneta:
    
#     def __init__(self, cor):
#         #private #protected #public ----> protegendo meus atributos
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())