from abc import abstractmethod
    
    
class Banco:
    agencia = 4136
    
    def add_cliente(self, cliente):
        if cliente.conta.agencia != self.agencia:
            print('Esta conta não pertence a este Banco.')
            return
        cliente.conta.permissao = True
        
    
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.conta = conta
    
    
class Conta:
    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    
class CC(Conta):
    limite = 1000
    permissao = False
    
    def sacar(self, valor):
        if self.saldo - valor < self.limite * -1 or not self.permissao:
            print('Você não tem permissão para sacar')
            return
        self.saldo -= valor
    
    
class CP(Conta):
    permissao = False
    
    def sacar(self, valor):
        if self.saldo - valor < 0 or not self.permissao:
            print('Você não tem permissão para sacar')
            return
        self.saldo -= valor
    
    
banco = Banco()
conta1 = CC(4136, 111111, 1000)
c1 = Cliente('Lucas', 17, conta1)
banco.add_cliente(c1)
c1.conta.sacar(500)
print(c1.nome)
print(c1.conta.saldo)
    
print()
    
conta2 = CP(4136, 213333, 300)
c2 = Cliente('João', 32, conta2)
banco.add_cliente(c2)
c2.conta.sacar(200)
print(c2.nome)
print(c2.conta.saldo)