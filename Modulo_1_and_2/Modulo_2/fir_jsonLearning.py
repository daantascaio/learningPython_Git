import json
import os

# pessoa = {
#       "nome": "Luiz Otávio 2",
#       "sobrenome": "Miranda",
#       "enderecos": [
#         {
#           "rua": "R1",
#           "numero": 32
#         },
#         {
#           "rua": "R2",
#           "numero": 55
#         }
#       ],
#       "altura": 1.8,
#       "numeros_preferidos": [
#         2,
#         4,
#         6,
#         8,
#         10
#       ],
#       "dev": True,
#       "nada": None
# }

# with open('Modulo_2\\first_Arq_Json.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#           pessoa, 
#           arquivo,
#           indent=2,
#         )

with open ('C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\Modulo_2\\first_Arq_Json.json', 'r', encoding='utf8') as arq:
    pessoa = json.load(arq)
    print(pessoa)

# os.rename('C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\first_Arq_Json.json', 'C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\Modulo_2\\first_Arq_Json.json')