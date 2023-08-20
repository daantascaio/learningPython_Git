import json
import os

# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados.


class People:

    def __init__(self, name, age, height, job):
        self.name = name
        self.age = age
        self.height = height
        self.job = job

# people_one = People('Caio', 20, 1.83, 'DevOps') # setting my instance data

# data_people_one = people_one.__dict__ # storing my instance data

# -- # -- #
# with open('Modulo_3_introPOO\\exercicios\\1exer_people_one.json', 'w', encoding='utf8') as json.file:
#     json.dump(
#         data_people_one,
#         json.file,
#         indent=2,
#     )
# -- # -- #

# -- # -- #
with open('Modulo_3_introPOO\\exercicios\\1exer_people_one.json', 'r', encoding='utf8') as json.file:
    people_one = json.load(json.file)

people_one = People(**people_one)
print(vars(people_one))
print(people_one.name)
print(people_one.age)
print(people_one.height)
print(people_one.job)



