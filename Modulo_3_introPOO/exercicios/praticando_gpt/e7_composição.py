"""
Exercício 7: Composição
Crie uma classe chamada Autor com atributos para nome, idade e nacionalidade. 
Em seguida, crie uma classe chamada Livro, com atributos para título, ano de publicação e um autor associado. 
Utilize a composição para relacionar um autor a um livro.
"""

class Autor:
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, ano_publicacao, autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor
    
    def imprimir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Autor: {self.autor.nome}")
        print(f"Idade do Autor: {self.autor.idade}")
        print(f"Nacionalidade do Autor: {self.autor.nacionalidade}")

# Criando uma instância da classe Autor
autor = Autor("J.K. Rowling", 56, "Reino Unido")

# Criando uma instância da classe Livro associada ao autor
livro = Livro("Harry Potter and the Sorcerer's Stone", 1997, autor)

# Imprimindo detalhes do livro e autor
livro.imprimir_detalhes()
