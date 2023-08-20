# Atributos de classe

class People:

    ano_atual = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age_borny(self):
        return People.ano_atual - self.age
    
people_one = People('Caio', 20)
# people_two = People('Isadora', 21)
# people_tre = People('Cecília', 1)
# print(people_one.get_age_borny())
# print(people_two.get_age_borny())
# print(people_tre.get_age_borny())

print(people_one.__dict__)