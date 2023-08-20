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

people_one = People('Caio', 20, 1.83, 'DevOps')
print(vars(people_one))

data_people_one = people_one.__dict__
print(data_people_one)

# -- # -- #
with open('Modulo_3_introPOO\\1exer_people_one.json', 'w', encoding='utf8') as arqs:
    json.dump(
        data_people_one,
        arqs,
        indent=2,
    )



