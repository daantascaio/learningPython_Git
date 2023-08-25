"""
Exercício 5: Polimorfismo
Crie uma classe abstrata chamada Animal com um método abstrato fazerSom(). 
Em seguida, crie classes derivadas como Cachorro, Gato e Vaca, cada uma implementando o método fazerSom() de maneira única.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def fazerSom(self):
        pass

class Cachorro(Animal):
    def fazerSom(self):
        return "Au au!"

class Gato(Animal):
    def fazerSom(self):
        return "Miau!"

class Vaca(Animal):
    def fazerSom(self):
        return "Muuu!"

# Criando instâncias das classes derivadas
rex = Cachorro("Rex")
felix = Gato("Felix")
mimosa = Vaca("Mimosa")

# Chamando o método fazerSom() de maneira polimórfica
animais = [rex, felix, mimosa]

for animal in animais:
    print(f"{animal.nome} faz: {animal.fazerSom()}")
