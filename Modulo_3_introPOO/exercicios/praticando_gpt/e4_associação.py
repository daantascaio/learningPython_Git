import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Círculo:
    def __init__(self, raio, centro):
        self.raio = raio
        self.centro = centro
    
    def calcular_area(self):
        return round(math.pi * self.raio ** 2, 2)
    
    def calcular_circunferencia(self):
        return round(2 * math.pi * self.raio, 2)
    
    def imprimir_detalhes(self):
        print("Detalhes do Círculo:")
        print(f"Raio: {self.raio}")
        print(f"Centro: ({self.centro.x}, {self.centro.y})")
        print(f"Área: {self.calcular_area()}")
        print(f"Circunferência: {self.calcular_circunferencia()}")

# Criando uma instância da classe Ponto para representar o centro do círculo
centro_do_circulo = Ponto(0, 0)

# Criando uma instância da classe Círculo associada ao ponto criado
circulo = Círculo(5, centro_do_circulo)

# Imprimindo detalhes do círculo
circulo.imprimir_detalhes()
