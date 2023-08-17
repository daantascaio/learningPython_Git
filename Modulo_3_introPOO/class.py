"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classes.

string = 'Luiz'  # str
print(string.upper())
print(isinstance(string, str))
"""


class People:
    ...


people_one = People()
people_one.firstName = 'Caio'
people_one.secondName = 'Dantas'

people_two = People()
people_two.firstName = 'Isadora'
people_two.secondName = 'Fiorentino'

print(people_one.firstName)
print(people_one.secondName)

print()

print(people_two.firstName)
print(people_two.secondName)

