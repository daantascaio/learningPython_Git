"""
Exercício 2: Herança
Crie uma classe chamada Aluno que herda da classe Pessoa (do exercício anterior). 
Adicione um atributo adicional para o número de matrícula do aluno. 
Sobrescreva o método de impressão para incluir o número de matrícula.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Aluno(Pessoa):  # Aqui, Aluno herda de Pessoa
    def __init__(self, nome, idade, matricula):  # Adicionamos o atributo matrícula
        super().__init__(nome, idade)  # Chamamos o construtor da classe base (Pessoa)
        self.matricula = matricula  # Inicializamos o atributo matrícula
    
    def imprimir_detalhes(self):  # Sobrescrevemos o método imprimir_detalhes
        super().imprimir_detalhes()  # Chamamos o método da classe base (Pessoa)
        print(f"Matrícula: {self.matricula}")

# Criando uma instância da classe Aluno
aluno1 = Aluno("Maria", 20, "2023-001")
aluno1.imprimir_detalhes()