import json
from exer1_saveClassInJSON_pt1 import PATH_FILE, People

with open(PATH_FILE, 'r', encoding='utf8') as json.file:
    people_one = json.load(json.file)

people_one = People(**people_one)
print(vars(people_one))
print(people_one.age)
print(people_one.job)