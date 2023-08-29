# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Atributos que começar com um ou dois underlines ( _, __ ) não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

# class Caneta:
#     def __init__(self, cor):
#         # private protected
#         self.cor = cor
#         self._cor_tampa = None

#     @property
#     def cor(self):
#         print('ESTOU NO GETTER')
#         return self._cor

#     @cor.setter
#     def cor(self, valor):
#         print('ESTOU NO SETTER')
#         self._cor = valor

#     @property
#     def cor_tampa(self):
#         return self._cor_tampa

#     @cor_tampa.setter
#     def cor_tampa(self, valor):
#         self._cor_tampa = valor


# caneta = Caneta('Azul')
# caneta.cor = 'Rosa'
# caneta.cor_tampa = 'Azul'
# print(caneta.cor)
# print(caneta.cor_tampa)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 3:
            print("O nome deve ter pelo menos 3 caracteres.")
        else:
            self._nome = novo_nome

# Criando uma instância da classe Pessoa
pessoa = Pessoa("João")

# Usando o setter para modificar o nome
pessoa.nome = "Ana"  # Isso funcionará

pessoa.nome = "Lu"  # Isso imprimirá uma mensagem de validação
