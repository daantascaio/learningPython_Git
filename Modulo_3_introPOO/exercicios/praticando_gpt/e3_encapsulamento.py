"""
Exercício 3: Encapsulamento
Crie uma classe chamada ContaBancaria. 
A classe deve ter atributos para o número da conta e o saldo. 
Implemente métodos para depositar dinheiro, sacar dinheiro e verificar o saldo.
"""

class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente para saque.")
    
    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: {self.saldo}")

# Criando uma instância da classe ContaBancaria
conta = ContaBancaria("12345", 1000)

# Realizando operações na conta
conta.depositar(500)
conta.sacar(200)
conta.verificar_saldo()
