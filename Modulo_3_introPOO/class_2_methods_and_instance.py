# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código


# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def acelerar(self):
        print(f'{self.name} está acelerando!\n')


fusca = Car('Fusca', 'Volkswagen')
print(f'Car Name: {fusca.name} || Car Brand: {fusca.brand}')
fusca.acelerar()


celta = Car('Celta', 'Chevrolet')
print(f'Car Name: {celta.name} || Car Brand: {celta.brand}')
celta.acelerar()