"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, ABCMeta, abstractclassmethod, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo = 0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor


class ContaCorrente(Conta):
    ...


class ContaPoupanca(Conta):
    ...   


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def get_nome(self):
        return self._nome
    
    @get_nome.setter
    @abstractmethod
    def get_nome(self, nome):...

    @property
    def get_idade(self):
        return self._idade
    
    @get_idade.setter
    @abstractmethod
    def get_idade(self, idade):...


class Banco(ABC):
    ...


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    @Pessoa.get_nome.setter
    def get_nome(self, nome):
        self._nome = nome

    @Pessoa.get_idade.setter
    def get_idade(self, idade):
        self._idade = idade


# cliente_id1= Cliente('Caio Dantas', 30)
# print(c1.get_idade)
# print(c1.get_nome)

t = Conta(123, 12345)
t.depositar(100)
print(t._saldo)





