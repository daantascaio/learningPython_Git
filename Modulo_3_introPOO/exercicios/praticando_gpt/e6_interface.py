"""
Exercício 6: Interface
Crie uma interface chamada FormaGeometrica com métodos abstratos para calcular a área e o perímetro. 
Implemente essa interface nas classes Quadrado, Círculo e Triângulo, cada uma 
calculando a área e o perímetro de acordo com sua forma específica.
"""

from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Criando instâncias das classes e calculando área e perímetro
quadrado = Quadrado(5)
circulo = Circulo(3)
triangulo = Triangulo(5, 6, 7)

print(f"Quadrado: Área = {quadrado.calcular_area()}, Perímetro = {quadrado.calcular_perimetro()}")
print(f"Círculo: Área = {circulo.calcular_area()}, Perímetro = {circulo.calcular_perimetro()}")
print(f"Triângulo: Área = {triangulo.calcular_area()}, Perímetro = {triangulo.calcular_perimetro()}")
