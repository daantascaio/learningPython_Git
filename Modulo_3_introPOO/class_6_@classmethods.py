# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemos a própria classe

class Pessoa:
    ano = 2023 # Atributo da classe 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_classe(self):
        print('Hey')

p1 = Pessoa('João', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()