"""
Exercício 1: Criando uma Classe Básica
Crie uma classe chamada Pessoa com os seguintes atributos: nome e idade. 
Implemente um método para imprimir os detalhes da pessoa.
"""

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # def imprimir_detalhes(self):
    #     print(self.nome, self.idade)

    def imprimir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa_1 = Pessoa('Caio', 20)
# pessoa_1.imprimir_detalhes()
pessoa_1.imprimir_detalhes()