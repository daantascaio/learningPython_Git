"""
Exercício 1: Agregação - Biblioteca e Livros

Crie uma classe chamada Livro com atributos para título, autor e ano de publicação. 
Em seguida, crie uma classe chamada Biblioteca que possui uma lista de livros como atributo. 
Implemente métodos para adicionar um livro à biblioteca e para listar todos os livros presentes.
"""

class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class Biblioteca:

    def __init__(self):
        self.livros = []

    def adiciona_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        print("Livros na Biblioteca:")
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")

livro_1 = Livro('O Amor é Doloroso', 'Ruim de Costa', 1990)
livro_2 = Livro('As Aventuras de Curim', 'Charles Babum', 2011)
livro_3 = Livro('Jacum, o Mistério', 'Frente Ruim', 1876)
livro_4 = Livro('Dor de Dente', 'Dante de Sabre Ferreira', 2000)
livro_5 = Livro('Caso Perdido', 'Catro Achado de Assis', 1659)

# Criando uma instância de Biblioteca
biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adiciona_livro(livro_1)
biblioteca.adiciona_livro(livro_2)
biblioteca.adiciona_livro(livro_3)
biblioteca.adiciona_livro(livro_4)
biblioteca.adiciona_livro(livro_5)

# Listando os livros na biblioteca
biblioteca.listar_livros()
