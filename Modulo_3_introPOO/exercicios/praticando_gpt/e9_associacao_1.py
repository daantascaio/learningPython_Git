"""
Exercício 2: Associação - Escola e Alunos

Crie uma classe chamada Aluno com atributos para nome, idade e nota. 
Crie outra classe chamada Escola que possui uma lista de alunos como atributo. 
Implemente métodos para adicionar um aluno à escola, calcular a média das notas 
dos alunos e exibir a lista de alunos.
"""

class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

class Escola:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def calcular_media_notas(self):
        total_notas = sum(aluno.nota for aluno in self.alunos)
        return total_notas / len(self.alunos) if self.alunos else 0
    
    def listar_alunos(self):
        print("Alunos na Escola:")
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Nota: {aluno.nota}")

# Criando instâncias de Aluno
aluno1 = Aluno("João", 15, 8.5)
aluno2 = Aluno("Maria", 16, 9.0)
aluno3 = Aluno("Pedro", 15, 7.8)

# Criando uma instância de Escola
escola = Escola()

# Adicionando alunos à escola
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
escola.adicionar_aluno(aluno3)

# Listando os alunos na escola
escola.listar_alunos()

# Calculando a média das notas dos alunos
media_notas = escola.calcular_media_notas()
print(f"Média das notas: {media_notas:.2f}")


