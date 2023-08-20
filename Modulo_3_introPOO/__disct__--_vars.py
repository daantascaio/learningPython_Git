# Atributos de classe

class People:

    ano_atual = 2023

    def __init__(self, name, age): # the name, age and other attributes to be added are saved in __dict__
        self.name = name
        self.age = age

    def get_age_borny(self):
        return People.ano_atual - self.age
    

data_Caio = {'name': 'Caio', 'age': 23}

people_one = People(**data_Caio)
print(vars(people_one))

# people_two = People('Isadora', 21)
# people_tre = People('Cecília', 1)
# print(people_one.get_age_borny())
# print(people_two.get_age_borny())
# print(people_tre.get_age_borny())

# people_one.__dict__['height'] = 1.83
# people_one.__dict__['age'] = 23
# print(people_one.__dict__)
# print(vars(people_one))
# print(people_one.height)