import json




PATH_FILE = 'C:\\Users\\elenice Ferreira\\Desktop\\learningPython_Git\\Modulo_3_introPOO\\exercicios\\exer1_RESOLUCTIONProf.json'



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Caio', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('João', 47)
bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(PATH_FILE, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()