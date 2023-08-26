"""
Exercício 3: Composição - Departamento e Funcionários

Crie uma classe chamada Funcionario com atributos para nome, cargo e salário. 
Crie outra classe chamada Departamento que possui uma lista de funcionários como atributo. 
Implemente métodos para adicionar um funcionário ao departamento, calcular o total de salários e listar os funcionários.
"""

class Funcionario:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Departamento:

    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def total_salarios(self):
        total = sum(i.salario for i in self.funcionarios)
        return print(f'TOTAL: ${total}')

    def listar_funcionarios(self):
        print('Funcionários:')
        for i in self.funcionarios:
            print(f'Nome: {i.nome} | Cargo: {i.cargo} Salário: {i.salario}')
            

funcionario_1 = Funcionario('Caio Dantas', 'SysAdmin', 7880)
funcionario_2 = Funcionario('Fernando Pereira', 'Faxineiro', 3000)
funcionario_3 = Funcionario('Ian Esquisito', 'Dev', 7000)
funcionario_4 = Funcionario('Kayo Frasco', 'Contador', 5000)
funcionario_5 = Funcionario('Froyd Dantas', 'Dev', 4000)

departamento = Departamento()

departamento.adicionar_funcionario(funcionario_1)
departamento.adicionar_funcionario(funcionario_2)
departamento.adicionar_funcionario(funcionario_3)
departamento.adicionar_funcionario(funcionario_4)
departamento.adicionar_funcionario(funcionario_5)

departamento.listar_funcionarios()

departamento.total_salarios()